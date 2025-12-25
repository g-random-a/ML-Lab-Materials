"""
Vercel serverless function entry point for Django application
"""
import os
import sys
from pathlib import Path
from io import BytesIO

# Add the project root to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'profit_predictor.settings')

# Import Django
import django
django.setup()

# Import WSGI application
from profit_predictor.wsgi import application

def handler(request):
    """
    Vercel serverless function handler that wraps Django WSGI application
    """
    # Handle different request formats (dict or object)
    if isinstance(request, dict):
        # Request is a dictionary (Vercel format)
        method = request.get('method', 'GET')
        path = request.get('path', '/')
        headers = request.get('headers', {})
        body = request.get('body', b'')
        query_string = request.get('queryStringParameters', {})
        if query_string:
            from urllib.parse import urlencode
            query_string = urlencode(query_string)
        else:
            query_string = ''
    else:
        # Request is an object
        method = getattr(request, 'method', 'GET')
        path = getattr(request, 'path', '/')
        headers = getattr(request, 'headers', {})
        body = getattr(request, 'body', b'')
        query_string = getattr(request, 'query_string', '')
    
    # Convert body to bytes if needed
    if isinstance(body, str):
        body = body.encode('utf-8')
    elif body is None:
        body = b''
    
    # Get host from headers
    host = headers.get('host', 'localhost')
    if ':' in host:
        server_name, server_port = host.split(':', 1)
    else:
        server_name = host
        server_port = '80'
    
    # Build WSGI environ dictionary
    environ = {
        'REQUEST_METHOD': method,
        'SCRIPT_NAME': '',
        'PATH_INFO': path,
        'QUERY_STRING': query_string,
        'CONTENT_TYPE': headers.get('content-type', ''),
        'CONTENT_LENGTH': str(len(body)),
        'SERVER_NAME': server_name,
        'SERVER_PORT': server_port,
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': headers.get('x-forwarded-proto', 'https'),
        'wsgi.input': BytesIO(body),
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': True,
        'wsgi.run_once': False,
    }
    
    # Add HTTP headers to environ
    for key, value in headers.items():
        key_upper = key.upper().replace('-', '_')
        if key_upper not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            environ[f'HTTP_{key_upper}'] = value
    
    # Response variables
    status_code = [200]
    response_headers_dict = {}
    
    def start_response(status, headers_list):
        status_code[0] = int(status.split()[0])
        response_headers_dict.update(dict(headers_list))
    
    # Call Django WSGI application
    try:
        response_body = application(environ, start_response)
        
        # Collect response body
        body_parts = []
        for chunk in response_body:
            if chunk:
                if isinstance(chunk, bytes):
                    body_parts.append(chunk)
                else:
                    body_parts.append(chunk.encode('utf-8'))
        
        body_bytes = b''.join(body_parts)
        
        # Return response in Vercel format
        return {
            'statusCode': status_code[0],
            'headers': response_headers_dict,
            'body': body_bytes.decode('utf-8', errors='ignore')
        }
    except Exception as e:
        # Return error response
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/plain'},
            'body': f'Internal Server Error: {str(e)}'
        }

