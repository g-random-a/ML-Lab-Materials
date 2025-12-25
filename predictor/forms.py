from django import forms

STATE_CHOICES = [
    ('California', 'California'),
    ('Florida', 'Florida'),
    ('New York', 'New York'),
]

class ProfitPredictionForm(forms.Form):
    rd_spend = forms.FloatField(
        label='R&D Spend',
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter R&D Spend (e.g., 91992.39)',
            'step': '0.01'
        })
    )
    
    administration = forms.FloatField(
        label='Administration',
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Administration Cost (e.g., 135495.07)',
            'step': '0.01'
        })
    )
    
    marketing_spend = forms.FloatField(
        label='Marketing Spend',
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Marketing Spend (e.g., 252664.93)',
            'step': '0.01'
        })
    )
    
    state = forms.ChoiceField(
        label='State',
        choices=STATE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )



