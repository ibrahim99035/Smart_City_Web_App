from keras.models import model_from_json
import cv2
import tensorflow as tf
import numpy as np
import tkinter as tk

def detect_emotions():
    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
    # load json and create model
    json_file = open('emotion_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights('emotion_model.h5')
    print("Loaded model from disk")
    # evaluate loaded model on test data
    loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    # load weights into new model
    print("Loaded model from disk")
    # start the webcam feed
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    cap=cv2.VideoCapture(0)
    while True:
        # Find haar cascade to draw bounding box around face
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if not ret:
            break
        # detect faces available on camera
        #num_faces =  face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # take each face available on the camera and Preprocess it
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
            roi_gray_frame = gray[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

            # predict the emotions
            emotion_prediction = loaded_model.predict(cropped_img)
            maxindex = int(np.argmax(emotion_prediction))
            cv2.putText(frame, emotion_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Emotion Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



def mask_detection():
    # Load the trained model
    model = tf.keras.models.load_model('mask_detector.h5')

    # Start the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame
        ret, frame = cap.read()

        # Detect faces in the frame
        face_cascade = cv2.CascadeClassifier('F:\python\python310\lib\site-packages\cv2\data\haarcascade_frontalface_default.xml ')
        if face_cascade.empty():
            print("Error loading classifier file")
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

        # Iterate over the faces
        for (x, y, w, h) in faces:
            # Crop the face from the frame
            face_img = frame[y:y + h, x:x + w]

            # Resize the image to match the model input size
            face_img = cv2.resize(face_img, (64, 64))

            # Convert the image to a 4D array
            face_img = np.expand_dims(face_img, axis=0)

            # Make a prediction
            prediction = model.predict(face_img)[0]

            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Draw a label indicating whether the person is wearing a mask
            if prediction[0] > 0.3:
                label = 'mask'
                color = (0, 255, 0)
            else:
                label = 'no Mask'
                color = (0, 0, 255)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        # Show the webcam stream
        cv2.imshow('Webcam', frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()


def run_patient_counter():
    doctors = {
        "Dr. Sara": 0,
        "Dr. Ahmed": 0,
        "Dr. Hanaa": 0,
        "Dr. Batool": 0,
        "Dr. Mahmed": 0
    }

    def add_patient(doctor):
        doctors[doctor] += 1
        return "You are patient number {} for {}".format(doctors[doctor], doctor)

    def update_patient_number(label, doctor):
        patient_number = add_patient(doctor)
        label.config(text=patient_number)

    def select_doctor():
        selected_doctor = var.get()
        update_patient_number(label, selected_doctor)

    root = tk.Tk()
    root.title("Patient Counter")
    root.geometry("400x400")

    label = tk.Label(root, text="Select a doctor to display the patient number", font=("Helvetica", 16))
    label.pack(pady=20)

    var = tk.StringVar()
    var.set("Choose your doctor")

    dropdown = tk.OptionMenu(root, var, *doctors.keys())
    dropdown.pack(pady=20)

    button = tk.Button(root, text="Next Patient", command=select_doctor, font=("Helvetica", 16), bg="light blue", height=2, width=20)
    button.pack(pady=20)

    root.mainloop()
detect_emotions()
mask_detection()
run_patient_counter()

