from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospital, name = 'hospital'), 
    path('braintumor/', views.braintumor, name = 'braintumor'),
    path('breastcancer/', views.breastcancer, name = 'breastcancer')
]