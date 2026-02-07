# 🥔 Potato Disease Detection

An end-to-end deep learning project that detects potato leaf diseases using a Convolutional Neural Network (CNN).

## 🔍 Problem Statement
Plant diseases can significantly reduce crop yield. This project aims to classify potato leaf images into different disease categories using deep learning.

## 🧠 Model Details
- Architecture: Custom CNN
- Framework: TensorFlow / Keras
- Classes:
  - Potato Early Blight
  - Potato Late Blight
  - Healthy Potato Leaf
- Validation Accuracy: ~94%

## 🌐 Web Application
The trained model is deployed as a Streamlit web application where users can upload a potato leaf image and get real-time predictions with confidence scores.

## 🛠 Tech Stack
- Python
- TensorFlow / Keras
- NumPy
- Streamlit
- Pillow

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
