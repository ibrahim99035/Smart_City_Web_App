from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def hospital(request):
    title = 'Diagnosing'
    return render(request, 'hospital.html', {'title': title})


#--------------------------------------------------------------------------------------------
#Diagnosing Functionality
import os
from werkzeug.utils import secure_filename
import tensorflow as tf 
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.utils import image_utils
from PIL import Image


import numpy as np
import pandas as pd 
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
    if request.method == 'POST':
        uploaded_file = request.FILES['brain']
        
        File_System = FileSystemStorage()
        if uploaded_file and allowed_file(uploaded_file.name):
            filename = secure_filename(uploaded_file.name)
            File_System.save(filename, uploaded_file)
        
        
        model = tf.keras.models.load_model(r'E:/FinalYear/Project/Ropositories/Smart_City_Web_App/City/BrainTumour/model.wdah_brain')   
        img = image_utils.load_img(r'upload_temp/'+ uploaded_file.name , target_size=(224, 224))
        x = image_utils.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        img_data = preprocess_input(x)
        classes = model.predict(img_data)
        New_pred = np.argmax(classes, axis=1)
        if New_pred==[1]:
           result ='Prediction: Negative'
        else:
           result = 'Prediction: Positive'
        if os.path.exists('upload_temp/'+ uploaded_file.name):
            os.remove('upload_temp/'+ uploaded_file.name)

    return render(request, 'braintumor.html', {'title': title, 'result': result})

def breastcancer(request):
    title = 'Brast Cancer'
    return render(request, 'breastcancer.html', {'title': title})



