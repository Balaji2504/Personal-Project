import tkinter as tk
import customtkinter as ck
import pandas as pd
import numpy as np
import pickle
import mediapipe as mp
import cv2
from PIL import Image, ImageTk
from landmarks import landmarks
import warnings

# Suppress scikit-learn future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

window = tk.Tk()
window.geometry("480x700")
window.title("Swoleboi")
ck.set_appearance_mode("dark")

def create_text_on_canvas(canvas, x, y, text, font=("Arial", 20), text_color="black"):
    canvas.create_text(x, y, text=text, font=font, fill=text_color)

# Create canvas and labels for STAGE
stage_canvas = tk.Canvas(window, height=40, width=120)
stage_canvas.place(x=10, y=1)
stage_label = create_text_on_canvas(stage_canvas, 60, 20, 'STAGE')

# Create canvas and labels for REPS
reps_canvas = tk.Canvas(window, height=40, width=120)
reps_canvas.place(x=160, y=1)
reps_label = create_text_on_canvas(reps_canvas, 60, 20, 'REPS')

# Create canvas and labels for PROB
prob_canvas = tk.Canvas(window, height=40, width=120)
prob_canvas.place(x=300, y=1)
prob_label = create_text_on_canvas(prob_canvas, 60, 20, 'PROB')

# Create canvas and labels for the dynamic values
stage_value_canvas = tk.Canvas(window, height=40, width=120)
stage_value_canvas.place(x=10, y=41)
stage_value_label = stage_value_canvas.create_text(60, 20, text='0', font=("Arial", 20), fill='blue')

reps_value_canvas = tk.Canvas(window, height=40, width=120)
reps_value_canvas.place(x=160, y=41)
reps_value_label = reps_value_canvas.create_text(60, 20, text='0', font=("Arial", 20), fill='blue')

prob_value_canvas = tk.Canvas(window, height=40, width=120)
prob_value_canvas.place(x=300, y=41)
prob_value_label = prob_value_canvas.create_text(60, 20, text='0', font=("Arial", 20), fill='blue')

def reset_counter():
    global counter
    counter = 0

button = ck.CTkButton(window, text='RESET', command=reset_counter, height=40, width=120, text_color="white", fg_color="blue")
button.place(x=10, y=600)

frame = tk.Frame(height=480, width=480)
frame.place(x=10, y=90)
lmain = tk.Label(frame)
lmain.place(x=0, y=0)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)

with open('deadlift.pkl', 'rb') as f:
    model = pickle.load(f)

# Try opening the default camera (index 0)
cap = cv2.VideoCapture(0)

current_stage = ''
counter = 0
bodylang_prob = np.array([0,0])
bodylang_class = ''

def detect():
    global current_stage
    global counter
    global bodylang_class
    global bodylang_prob

    ret, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(106,13,173), thickness=4, circle_radius = 5),
            mp_drawing.DrawingSpec(color=(255,102,0), thickness=5, circle_radius = 10))

        try:
            row = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten().tolist()
            X = pd.DataFrame([row], columns=landmarks)
            bodylang_prob = model.predict_proba(X)[0]
            bodylang_class = model.predict(X)[0]

            if bodylang_class == "down" and bodylang_prob[bodylang_prob.argmax()] > 0.7:
                current_stage = "down"
            elif current_stage == "down" and bodylang_class == "up" and bodylang_prob[bodylang_prob.argmax()] > 0.7:
                current_stage = "up"
                counter += 1

        except Exception as e:
            print(e)

    img = image[:, :460, :]
    imgarr = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(imgarr)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, detect)

    # Update the labels
    stage_value_canvas.itemconfig(stage_value_label, text=current_stage)
    reps_value_canvas.itemconfig(reps_value_label, text=str(counter))
    prob_value_canvas.itemconfig(prob_value_label, text=str(bodylang_prob[bodylang_prob.argmax()]))

detect()
window.mainloop()