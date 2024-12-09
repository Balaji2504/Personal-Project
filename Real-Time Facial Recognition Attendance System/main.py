import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import pickle
import pyttsx3  # For voice feedback

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speech rate

# Paths for images and unknown faces
path = './student_images'
unknown_faces_dir = './unknown_faces'
os.makedirs(unknown_faces_dir, exist_ok=True)

# Load images and extract class names
images = []
classNames = []
mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

# Function to encode faces
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)
        if len(encoded_face) > 0:
            encodeList.append(encoded_face[0])
    return encodeList

# Load or generate face encodings
if os.path.exists('encodings.pkl'):
    with open('encodings.pkl', 'rb') as file:
        encoded_face_train = pickle.load(file)
else:
    encoded_face_train = findEncodings(images)
    with open('encodings.pkl', 'wb') as file:
        pickle.dump(encoded_face_train, file)

# Mark attendance
def markAttendance(name):
    date = datetime.now().strftime('%d-%B-%Y')
    filename = f'Attendance_{date}.csv'
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write('Name,Time,Date\n')
    with open(filename, 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S %p')
            f.writelines(f'{name},{time},{date}\n')
            engine.say(f"Attendance registered for {name}")
            engine.runAndWait()

# Set to track recorded names in the current session
recordedNames = set()
unknownCount = 0

# Initialize face detection for optimization (optional step)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Real-time webcam feed
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    if not success:
        print("Failed to access the webcam. Exiting...")
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

    for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        matchIndex = np.argmin(faceDist)

        # Default label and color for unknown person
        label = "Unknown Person"
        color = (0, 0, 255)  # Red for unknown

        if matches[matchIndex] and faceDist[matchIndex] < 0.6:
            name = classNames[matchIndex]
            if name not in recordedNames:
                recordedNames.add(name)
                markAttendance(name)
                label = f"{name} - Attendance Registered"
            else:
                label = f"{name} - Attendance Registered"
            color = (0, 255, 0)  # Green for recognized person
        else:
            # Save unknown face
            now = datetime.now()
            timestamp = now.strftime('%Y%m%d_%H%M%S')
            unknown_file = f"{unknown_faces_dir}/unknown_{timestamp}.jpg"
            cv2.imwrite(unknown_file, img)
            label = "Unknown Person"
            unknownCount += 1
            engine.say("Unknown person detected")
            engine.runAndWait()

        # Draw rectangle and label
        y1, x2, y2, x1 = faceloc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), color, cv2.FILLED)
        cv2.putText(img, label, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    # Display real-time statistics
    totalRecognized = len(recordedNames)
    cv2.putText(img, f"Recognized: {totalRecognized}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(img, f"Unknowns: {unknownCount}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Webcam', img)

    # Check if 'q' is pressed to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        engine.say("Camera stopped. Goodbye!")
        engine.runAndWait()
        break

# Release resources and close all windows
cap.release()
cv2.destroyAllWindows()
