from django import forms
from predict_risk.models import Predictions

class Predict_Form(forms.ModelForm):
    class Meta:
        model = Predictions
        fields = ('age','gender','cp','resting_bp','serum_cholesterol','fasting_blood_sugar','resting_ecg','max_heart_rate', 'exercise_induced_angina','st_depression','st_slope')
        widgets = {'age': forms.TextInput(attrs={'class': 'form-control'}),
                   'gender': forms.Select(attrs={'class': 'form-control'}),
                   'cp': forms.Select(attrs={'class': 'form-control'}),
                   'resting_bp':forms.TextInput(attrs={'class': 'form-control'}),
                   'serum_cholesterol':forms.TextInput(attrs={'class': 'form-control'}),
                   'fasting_blood_sugar':forms.Select(attrs={'class': 'form-control'}),
                   'resting_ecg':forms.Select(attrs={'class': 'form-control'}),
                   'max_heart_rate':forms.TextInput(attrs={'class': 'form-control'}),
                   'exercise_induced_angina':forms.Select(attrs={'class': 'form-control'}),
                   'st_depression':forms.TextInput(attrs={'class': 'form-control'}),
                   'st_slope':forms.Select(attrs={'class': 'form-control'}),
                   }
