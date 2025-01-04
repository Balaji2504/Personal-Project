# **Real-Time Facial Recognition Attendance System**

## **Overview**
This project is a **Real-Time Facial Recognition Attendance System** that automates the process of tracking attendance using advanced facial recognition technology. The system dynamically creates daily attendance logs, provides voice feedback for user interaction, and saves images of unregistered individuals for review. It is optimized for real-time performance and offers a user-friendly interface.

---

## **Features**
- **Real-Time Face Recognition**: Detects and recognizes faces accurately using the `face_recognition` library.
- **Dynamic Attendance Logs**: Automatically creates and updates daily attendance files in CSV format.
- **Handling Unknown Individuals**: Saves images of unregistered faces to a folder for later review.
- **Voice Feedback**: Provides auditory feedback to confirm attendance status.
- **Performance Optimization**: Ensures smooth and real-time video feed processing.
- **User-Friendly Interface**: Displays labeled bounding boxes for recognized and unrecognized faces.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - `OpenCV` - for real-time video processing.
  - `face_recognition` - for face detection and recognition.
  - `NumPy` - for numerical computations.
  - `pyttsx3` - for text-to-speech voice feedback.

---

## **Installation**

### Prerequisites
1. Install Python (3.8 or later).
2. Ensure a webcam is connected to your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/real-time-attendance-system.git
   cd real-time-attendance-system
## **Usage**
1. Launch the application to start the webcam feed.
2. The system will:
   - Recognize registered individuals and mark their attendance.
   - Label unregistered individuals as "Unknown Person" and save their images.
   - Provide voice feedback for both scenarios.
3. Press `q` to quit the application.

## Project Structure
```
real-time-attendance-system/
├── student_images/         # Folder containing images of registered individuals
├── Attendance/             # Folder where daily attendance logs are saved
├── Unknown/                # Folder where unknown face images are stored
├── encodings.pkl           # File storing pre-computed facial encodings
├── Main.py                 # Main program file
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## **Example Workflow**
1. **Recognition**: The webcam captures live video frames.
2. **Matching**: The system compares detected faces with pre-trained encodings.
3. **Logging Attendance**:
   - If the person is recognized, their attendance is marked.
   - If the person is unrecognized, their image is saved.
4. **Voice Feedback**: Confirms attendance registration or notifies of an unknown individual.

---

## **Contributing**
Contributions are welcome! If you'd like to improve this project, please fork the repository, make your changes, and submit a pull request.

---

## **Acknowledgments**
Special thanks to:
- The developers of the `face_recognition` and `OpenCV` libraries for their powerful tools.
- The Python community for extensive resources and support.

---

## **Future Enhancements**
- Integration with cloud storage for attendance data.
- Multi-camera support for large-scale setups.
- Improved security measures for sensitive data handling.

---
