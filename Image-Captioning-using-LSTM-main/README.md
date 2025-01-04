# Image Captioning using LSTM

## Overview
This project demonstrates the creation of an image captioning system using a combination of a pre-trained VGG16 model for feature extraction and an LSTM-based neural network for caption generation. It integrates a user-friendly interface developed with Streamlit, making the system accessible for end-users to upload images and receive descriptive captions.

---

## Key Features
- **Dataset**: Utilizes the Flickr8k dataset containing images and corresponding captions.
- **Feature Extraction**: Employs the VGG16 model to extract features from images by removing its final layer.
- **Caption Preprocessing**: Processes and cleans image descriptions to create a uniform vocabulary corpus.
- **LSTM Model**: Combines image features and text sequences to generate captions word by word.
- **Evaluation**: Measures caption quality using the BLEU score.
- **Streamlit UI**: Provides an interactive interface for image upload and caption generation.

---

## Technologies Used
- **Programming Language**: Python
- **Deep Learning Framework**: TensorFlow
- **User Interface**: Streamlit

---

## Project Workflow

### 1. Dataset
The Flickr8k dataset, which consists of 8,000 images paired with descriptive captions, is used for this project. Captions serve as the ground truth for training and evaluating the model.

### 2. Feature Extraction with VGG16
- The VGG16 model, a pre-trained Convolutional Neural Network (CNN), is used as a feature extractor.
- The final layer of VGG16 is removed, enabling the extraction of intermediate features from input images.

### 3. Data Preprocessing
#### Description Cleaning:
- Text is converted to lowercase.
- Punctuation is removed.
- Only alphabetic characters are retained.

#### Vocabulary Creation:
- A vocabulary corpus is generated from the cleaned descriptions.
- Processed descriptions are saved for future use.

### 4. Data Preparation for LSTM
- **Input Generation**:
  - Two inputs are created for the model:
    1. Image features extracted using VGG16.
    2. Input text sequence to predict the next word.
- **Padding**:
  - Input sequences are padded with zeros to ensure consistent length.
- **One-Hot Encoding**:
  - Output sequences are one-hot encoded based on the vocabulary size.

### 5. LSTM Model Architecture
- **Input Layers**:
  - Image features input.
  - Text sequence input.
- **Processing Steps**:
  - Image features are passed through a dropout layer and dense layer.
  - Input sequences are passed through an embedding layer, followed by dropout and LSTM layers.
- **Feature Fusion**:
  - Outputs from both inputs are concatenated and processed through dense layers to predict the next word.

### 6. Model Compilation and Training
- The model is compiled with:
  - **Loss Function**: Categorical cross-entropy.
  - **Optimizer**: Adam.
- Training is conducted for 20 epochs to minimize loss and improve accuracy.

### 7. Prediction and Evaluation
- **Caption Generation**:
  - Captions are generated word by word until a stopping condition is met.
- **Evaluation**:
  - BLEU scores are used to assess the similarity between machine-generated captions and reference captions.
  - Corpus BLEU scores evaluate the model's overall performance.

### 8. Streamlit User Interface
- **Functionality**:
  - Allows users to upload images.
  - Extracts features using VGG16.
  - Predicts captions word by word using the LSTM model.
  - Displays the generated caption on the interface.

---

## Installation and Setup

### Prerequisites
1. Python 3.8 or higher installed.
2. TensorFlow and Streamlit installed.
3. Download and extract the Flickr8k dataset.

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Balaji2504/Personal-Project/tree/main/Image-Captioning-using-LSTM-main
   cd image-captioning-lstm
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Dataset**:
   - Place the Flickr8k dataset in the specified folder.
   - Run the preprocessing script to clean and save descriptions.

4. **Train the Model**:
   - Extract features using VGG16.
   - Train the LSTM model using the prepared data.

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

6. **Access the Application**:
   - Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Project Structure
```
image-captioning-lstm/
├── Image Captioning.ipynb   # Jupyter notebook with full workflow
├── app.py                   # Streamlit application
├── descriptions.txt         # Cleaned and preprocessed captions
├── Prediction.png           # Sample prediction result image
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
```

---

## Example
1. **Upload an Image**: Drag and drop or select an image file.
2. **Generated Caption**: View the machine-generated caption below the image.

---

## Acknowledgments
- **TensorFlow**: For providing tools to build and train the model.
- **Streamlit**: For creating an intuitive user interface.
- **Flickr8k Dataset**: For serving as the foundational dataset for the project.

---

## License
This project is licensed under the MIT License.
