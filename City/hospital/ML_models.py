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

class ModelProcess:
    def load_model(self, model_file):
        loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
        return loaded_model
    
    def getBrainResult(self, uploaded_file):
        model = tf.keras.models.load_model('BrainTumour/model.wdah_brain')   
        img = image_utils.load_img('upload_temp/'+ uploaded_file , target_size=(224, 224))
        x = image_utils.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        img_data = preprocess_input(x)
        classes = model.predict(img_data)
        New_pred = np.argmax(classes, axis=1)
        if New_pred==[1]:
            return'Prediction: Negative'
        else:
            return 'Prediction: Positive'

    
