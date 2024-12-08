# Celebrity Face Recognition System

This project showcases my proficiency in developing a robust machine learning model for celebrity face recognition, employing Python, PyCharm, and Visual Studio Code to deliver accurate and efficient results. The foundation of this endeavor lies in the utilization of powerful libraries such as Numpy, OpenCV, and Sklearn for the creation and training of the facial recognition model.

The primary focus was on training the model using images of sports personalities, a task that demanded meticulous attention to detail. Through careful implementation and tuning, the model achieved impressive accuracy in classifying and recognizing celebrity faces, underscoring its effectiveness in real-world applications.

In addition to the core machine learning aspect, this project embraces a holistic approach with a keen eye on data visualization and user interface. I utilized Matplotlib and Seaborn for creating visually compelling representations of the data, enhancing the interpretability of the model's performance. The integration of Flask, HTML, CSS, and Javascript further transformed the project into a dynamic web application, providing users with an interactive and user-friendly interface for celebrity face recognition.

This Celebrity Face Recognition System is a testament to my comprehensive skill set, from building and training machine learning models to crafting engaging and intuitive web applications. It not only demonstrates my technical proficiency in Python and related libraries but also reflects my commitment to delivering innovative solutions that bridge the gap between cutting-edge technology and user-friendly applications.

# This project showcases a machine learning application for classifying sports personalities. The model is restricted to recognizing five individuals:  
- **MS Dhoni**  
- **Lionel Messi**  
- **Cristiano Ronaldo**  
- **Sania Mirza**  
- **Smriti Mandhana**  

The project combines data science, machine learning, and web development to create an interactive and efficient system.

## 🗂️ Folder Structure
The folder structure of the project is as follows:
- **📂 UI**: Contains the frontend code using HTML, CSS, and JavaScript for the web interface.  
- **📂 haarcascades**: Includes pre-trained Haar Cascade models used for face detection.  
- **📂 server**: Contains the Flask server implementation for backend functionality.  
- **📄 CFRecognition_projects.ipynb**: A Jupyter notebook for model training, evaluation, and visualization.  
- **📦 DataSet.zip**: A compressed file with the dataset used for training and testing the model.  
- **📂 best_clf**: Directory containing files for the best classifier model.  
- **📄 class_dictionary.json**: A JSON file mapping class labels to their corresponding celebrity names.  
- **📄 saved_model.pkl**: The serialized trained model file for deployment purposes.

## 🚀 Technologies Used
- **Python**: Core programming language.
- **Numpy** & **OpenCV**: Data cleaning and preprocessing.
- **Matplotlib** & **Seaborn**: Data visualization.
- **Sklearn**: Model building and evaluation.
- **Flask**: Backend HTTP server.
- **HTML**, **CSS**, & **JavaScript**: Frontend UI development.
- **Jupyter Notebook**, **Visual Studio Code**, & **PyCharm**: IDEs used for development.

## 🧪 Model Development
The project employs a machine learning model to classify images of the listed sports personalities. The model was trained on a dataset created using a custom **Google image scraping script**, and preprocessing was done using **OpenCV** and **Numpy**.

## 🌟 Features
- **Dynamic Dataset Creation**: Scraped images using a custom Python script.
- **Interactive Web Application**: Flask-based backend with a user-friendly frontend interface.
- **Comprehensive Data Visualizations**: Performance evaluation using Matplotlib and Seaborn.
- **Accurate Classification**: Model trained to recognize the faces of five sports personalities with high precision.

## 📈 Workflow
1. **Data Collection**: Google image scraping for dataset creation.
2. **Data Preprocessing**: Cleaning and normalizing images using OpenCV.
3. **Model Building**: Developed using Scikit-learn and evaluated for accuracy.
4. **Web Integration**: Flask for backend logic and UI built with HTML/CSS/JavaScript.

## 🔧 How to Use
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Celebrity-Face-Recognition.git
   cd Celebrity-Face-Recognition

