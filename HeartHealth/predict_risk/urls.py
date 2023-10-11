from django.urls import path
from . import views
app_name='predict'
urlpatterns=[
path('<int:pk>/', views.PredictRisk, name='predict'),
]
