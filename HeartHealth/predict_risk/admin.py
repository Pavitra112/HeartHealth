from django.contrib import admin
from predict_risk.models import Predictions
# from django import forms

# class Prediction(admin.ModelAdmin):
#     list_display=('profile','age','gender','cp','resting_bp','serum_cholesterol','fasting_blood_sugar','resting_ecg','max_heart_rate','exercise_induced_angina','st_depression','st_slope','predicted_on','num')
admin.site.register(Predictions)