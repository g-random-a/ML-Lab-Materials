# Django Profit Predictor

A Django web application that demonstrates a machine learning model for predicting company profit based on R&D Spend, Administration costs, Marketing Spend, and State.

## Features

- 🎯 Interactive web interface with Django templates
- 🤖 Machine learning model integration (scikit-learn)
- 💰 Real-time profit predictions

## Model Information

- **Model Type**: scikit-learn Pipeline (OneHotEncoder + LinearRegression)
- **Input Features**:
  - R&D Spend (numeric)
  - Administration (numeric)
  - Marketing Spend (numeric)
  - State (categorical: California, Florida, New York)
- **Target**: Profit
- **Model Performance**:
  - R² Score: 0.94
  - MAE: 7395.43
  - RMSE: 84826955.04

## Prerequisites

- Python 3.8 or higher
- pip
- Ubuntu (or any Linux distribution)

## Setup Instructions

### Option 1: Using the Setup Script (Recommended)

1. Make the setup script executable:
   ```bash
   chmod +x setup.sh
   ```

2. Run the setup script:
   ```bash
   ./setup.sh
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### Option 2: Manual Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure the virtual environment is activated:
   ```bash
   source venv/bin/activate
   ```

2. Run database migrations (if needed):
   ```bash
   python manage.py migrate
   ```

3. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

4. Open your web browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## Project Structure

```
class/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── setup.sh                  # Setup script
├── README.md                 # This file
├── profit_predictor/         # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── predictor/                # Django app
│   ├── __init__.py
│   ├── apps.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── predictor/
│           ├── base.html
│           ├── index.html
│           └── result.html
└── model_bundle (1)/         # Model files
    ├── model.joblib
    ├── schema.json
    ├── metadata.json
    ├── example_inputs.json
    └── golden_outputs.json
```

## Usage

1. Navigate to the home page
2. Fill in the form with:
   - R&D Spend (e.g., 91992.39)
   - Administration cost (e.g., 135495.07)
   - Marketing Spend (e.g., 252664.93)
   - Select a State (California, Florida, or New York)
3. Click "Predict Profit"
4. View the predicted profit value

## Example Inputs

You can use the following example inputs from the model bundle:

- R&D Spend: 91992.39, Administration: 135495.07, Marketing Spend: 252664.93, State: California
- R&D Spend: 38558.51, Administration: 82982.09, Marketing Spend: 174999.3, State: California
- R&D Spend: 61994.48, Administration: 115641.28, Marketing Spend: 91131.24, State: Florida


