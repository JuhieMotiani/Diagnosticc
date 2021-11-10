from tensorflow import keras
import cv2
import numpy as np

model = keras.models.load_model("model/CPN_Model.h5")
resize = 150

def preprocess_image(image):
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
    image = cv2.resize(image, (resize, resize)) /255
    image = np.array(image)
    image = np.expand_dims(image, axis=0)
    return image

def prediction(image):
    image = preprocess_image(image)
    output = model.predict(image)
    output = np.argmax(output,axis=1)
    if output == 0:
        return 'COVID-19'
    elif output == 1:
        return 'Normal'
    else:
        return 'Pneumonia'