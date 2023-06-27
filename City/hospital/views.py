from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from werkzeug.utils import secure_filename
from hospital.ML_models import ModelProcess
from hospital.allowedImage import AllowedFiles
from rest_framework.response import Response
from rest_framework.decorators import api_view
from hospital.models import Employee, Department
from hospital.serializers import EmployeeSerializer, DepartmentSerializer


def hospital(request):
    title = 'Diagnosing'
    isHospital = True
    return render(request, 'hospital.html', {'title': title, 'isHospital': isHospital})

#Diagnosing Functionality
def braintumor(request):
    title = 'Brain Tumor'
    result = ''
    isHospital = True
    brainObject = ModelProcess()
    allowedFileObject = AllowedFiles()
    if request.method == 'POST':
        uploaded_file = request.FILES['brain']
        
        File_System = FileSystemStorage()
        if uploaded_file and allowedFileObject.allowed_file(uploaded_file.name):
            filename = secure_filename(uploaded_file.name)
            File_System.save(filename, uploaded_file)
        
        target_file = uploaded_file.name
        result = brainObject.getBrainResult(target_file)
        
        if os.path.exists('upload_temp/'+ uploaded_file.name):
            os.remove('upload_temp/'+ uploaded_file.name)

    return render(request, 'braintumor.html', {'title': title, 'result': result, 'isHospital': isHospital})

def breastcancer(request):
    isHospital = True
    title = 'Brast Cancer'
    return render(request, 'breastcancer.html', {'title': title, 'isHospital': isHospital})

@api_view(['GET'])
def getEmployees(request):
    Employees = Employee.objects.all()
    serializer = EmployeeSerializer(Employees, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postEmployee(request):
    serializer = EmployeeSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getDepartments(request):
    Departments = Department.objects.all()
    serializer = DepartmentSerializer(Departments, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postDepartment(request):
    serializer = DepartmentSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

