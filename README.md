# Traffic Sign Recognition System

## Overview

This project implements a traffic sign recognition system using deep learning. It classifies traffic signs from images and provides real-time predictions through a web application interface. The system is designed to be robust, scalable, and suitable for deployment.

---

## Features

* Traffic sign classification using deep learning
* Transfer learning with MobileNetV2 and ResNet50
* Advanced data augmentation for improved generalization
* Class imbalance handling using weighted training
* Model evaluation using confusion matrix analysis
* Web-based interface for image upload and prediction
* Displays predicted class with confidence score

---


## Model Improvements

### Transfer Learning

* MobileNetV2 for lightweight and real-time performance
* ResNet50 for improved accuracy

### Data Augmentation

Implemented using Albumentations:

* Brightness and contrast adjustment
* Rotation and scaling
* Motion blur and noise
* Horizontal flipping
* CLAHE and gamma correction

### Class Imbalance Handling

* Computed class weights during training
* Ensures balanced learning across all traffic sign classes

### Evaluation

* Confusion matrix used for performance analysis
* Helps identify misclassification patterns

---

## Installation

```bash
git clone <repository-url>
cd traffic-sign-recognition
pip install -r requirements.txt
```

---

## Training

```bash
python src/training/train.py
```

---

## Testing

```bash
python tests/test_model.py
```

---

## Running the Web Application

```bash
cd web_app
python app.py
```

Then open a browser and go to:

```
http://127.0.0.1:5000/
```

---

## Web Application Features

* Upload traffic sign image
* Drag and drop interface
* Displays predicted class label
* Shows prediction confidence score

---

## Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* Albumentations
* Flask
* NumPy, Matplotlib, Seaborn

---

## Future Improvements

* Real-time detection using video stream
* Integration with object detection models (YOLO)
* Deployment on edge devices (Raspberry Pi, mobile)
* Integration with autonomous vehicle systems

---

## Conclusion

This project demonstrates a complete pipeline from data preprocessing to model deployment. It focuses on building a robust and scalable traffic sign recognition system with practical deployment capabilities.
