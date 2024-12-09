# Deadlift Machine Learning Application 🏋️‍♂️

## Project Overview
The **Deadlift Machine Learning Application** is a real-time desktop application designed to track and evaluate deadlift movements. Using Mediapipe for pose detection and a pre-trained machine learning model, it classifies the user's posture during deadlift exercises as "up" or "down" and counts the repetitions with high accuracy. The project integrates **Tkinter** and **CustomTkinter** to create an interactive graphical user interface (GUI) for seamless user interaction.

---

## Features
- **Real-Time Pose Detection**: Utilizes Mediapipe to detect human pose landmarks.
- **Deadlift Classification**: Classifies user posture into "up" or "down" stages using a trained machine learning model (`deadlift.pkl`).
- **Repetition Counter**: Automatically counts and updates the number of deadlift repetitions.
- **Probability Display**: Shows the confidence level (probability) for the current classification.
- **Reset Functionality**: Allows the user to reset the repetition counter through a button.
- **Interactive GUI**: Designed with Tkinter and CustomTkinter for an intuitive user experience.

---

## Folder Structure
- **📄 app.py**: Main application script for GUI and functionality.
- **📄 landmarks.py**: Defines pose landmark configurations used for processing.
- **📄 deadlift.pkl**: Pre-trained machine learning model for deadlift classification.
- **📄 requirements.txt**: List of dependencies required to run the application.

---

## Technologies Used
- **Programming Language**: Python  
- **Libraries**: 
  - Mediapipe: Pose detection and landmark tracking  
  - OpenCV: Image processing and camera input  
  - NumPy & Pandas: Data manipulation and processing  
  - Scikit-learn: Machine learning model usage  
  - Tkinter & CustomTkinter: GUI design  
  - PIL (Pillow): Image handling for GUI integration  

---

## How It Works
1. The application uses Mediapipe's pose detection to identify key landmarks on the user's body during the exercise.
2. It processes these landmarks and passes them to a pre-trained machine learning model (`deadlift.pkl`) to classify the movement as either "up" or "down."
3. The GUI displays:
   - The current stage of the deadlift (up/down).  
   - The total repetitions completed.  
   - The probability confidence of the classification.  
4. A reset button allows the user to reset the repetition counter when needed.

---

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-link>
   cd Deadlift-Machine-Learning-Application
