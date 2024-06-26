import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D

def detect_emotion():
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    emotion_model = Sequential()
    emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
    emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    emotion_model.add(Dropout(0.25))
    emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    emotion_model.add(Dropout(0.25))
    emotion_model.add(Flatten())
    emotion_model.add(Dense(1024, activation='relu'))
    emotion_model.add(Dropout(0.5))
    emotion_model.add(Dense(7, activation='softmax'))
    emotion_model.load_weights('model.h5')

    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

    cap = cv2.VideoCapture(0)
    emotion = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_rects = face_cascade.detectMultiScale(frame_gray, 1.3, 5)

        for (x, y, w, h) in face_rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = frame_gray[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
            prediction = emotion_model.predict(cropped_img)
            max_index = int(np.argmax(prediction))
            emotion = emotion_dict[max_index]
            cv2.putText(frame, emotion, (x + 20, y - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('Emotion Detection', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            cv2.imwrite("snapshot.jpg", frame)
            print("Snapshot captured!")
            break

        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    print("Detected Emotion:", emotion)
    return emotion


