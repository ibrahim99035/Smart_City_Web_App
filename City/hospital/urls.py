from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospital, name = 'hospital'), 
    path('braintumor/', views.braintumor, name = 'braintumor'),
    path('breastcancer/', views.breastcancer, name = 'breastcancer'),
    path('api/get_empolyees', views.getEmployees, name = 'Get_Employees'),
    path('api/add_employee', views.postEmployee, name = 'Add_Employee'),
]