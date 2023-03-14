from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from hospital.ML_models import ModelProcess
def hospital(request):
    title = 'Diagnosing'
    isHospital = True
    return render(request, 'hospital.html', {'title': title, 'isHospital': isHospital})


#--------------------------------------------------------------------------------------------
#Diagnosing Functionality
import os
from werkzeug.utils import secure_filename

import joblib

def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

#--------------------------------------------------------------------------------------------
def braintumor(request):
    title = 'Brain Tumor'
    result = ''
    isHospital = True
    brainObject = ModelProcess()
    if request.method == 'POST':
        uploaded_file = request.FILES['brain']
        
        File_System = FileSystemStorage()
        if uploaded_file and allowed_file(uploaded_file.name):
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



