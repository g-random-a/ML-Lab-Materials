from django.shortcuts import render
from django.conf import settings
import joblib
import json
import os
from .forms import ProfitPredictionForm


MODEL_PATH = os.path.join(settings.MODEL_BUNDLE_PATH, 'model.joblib')
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print(f"Error loading model: {e}")



def index(request):
    """Display the prediction form."""
    form = ProfitPredictionForm()
    return render(request, 'predictor/index.html', {'form': form})

def predict(request):
    """Handle prediction request."""
    if request.method == 'POST':
        form = ProfitPredictionForm(request.POST)
        if form.is_valid():
            
            
            # Prepare input data
            input_data = {
                'R&D Spend': form.cleaned_data['rd_spend'],
                'Administration': form.cleaned_data['administration'],
                'Marketing Spend': form.cleaned_data['marketing_spend'],
                'State': form.cleaned_data['state']
            }

            import pandas as pd
            input_df = pd.DataFrame([input_data])
            # Make prediction
            if model:
                prediction = model.predict(input_df)
            else:
                prediction = None

            template_input_data = {
            'rd_spend': input_data['R&D Spend'],
            'administration': input_data['Administration'],
            'marketing_spend': input_data['Marketing Spend'],
            'state': input_data['State']
            }
            return render(request, 'predictor/result.html', {
                'prediction': round(prediction[0], 2) if prediction is not None else 20.0,
                'input_data': template_input_data,
                'form': form
            })
    else:
        form = ProfitPredictionForm()
    
    return render(request, 'predictor/index.html', {'form': form})

