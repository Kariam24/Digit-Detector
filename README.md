# Digit-Detector

By: Kariam Rodriguez, Yanni Pierre, Izze Lino, Sebastian Barrera

Course: CAP 4630

📌 Project Overview

This project focuses on building a neural network model that can accurately recognize handwritten digits (0–9). The goal is to demonstrate how deep learning can be applied to real-world image recognition tasks and to create an interactive way for users to draw digits and receive predictions.

🎯 Objectives
Problem

Computers struggle to interpret human handwriting accurately.

We aimed to create an AI model capable of reading handwritten digits (0–9).

Why It Matters

Powers technologies such as check readers, postal address scanners, and digitized forms.

Demonstrates how AI can learn and recognize human writing styles.

Goal

Train a highly accurate model that can classify handwritten digits.

Show how Artificial Neural Networks can be applied to image recognition.

Build an interface where users can draw digits and view predictions.

🧠 System Description

Dataset

MNIST dataset: 70,000 grayscale digit images (28×28 pixels)

60,000 training samples and 10,000 test samples

Model Type

Convolutional Neural Network (CNN) using TensorFlow/Keras

Why CNN

Designed specifically for image recognition

Consistently high accuracy on handwritten digit classification

Automatically detects and learns key visual patterns

Preprocessing

Normalized pixel values to range (0–1)

Flattened images into 1D arrays

⚙️ Methodology / Pipeline
Data Input → Preprocessing → Model Training → Evaluation → Prediction Output

Steps

Split MNIST data into training and testing

Trained model using Adam optimizer

Evaluated accuracy and loss performance

Evaluation Metric

Accuracy (balanced class dataset)

🧩 Model Architecture
Layers Used

3 Convolutional layers: 32, 64, 128 filters

ReLU activation

Batch Normalization

Max Pooling (2×2)

Dropout layers: 0.25, 0.35, 0.45

Output: Dense(10, Softmax) for digit classification

Training Setup

Optimizer: Adam

Loss Function: Sparse Categorical Crossentropy

Training Results

Final Training Accuracy: 99.39%

Validation Accuracy: 99.51%

📈 Implementation Results
Observations

Model generalized well

Small gap between training and validation loss → minimal overfitting

High performance on unseen handwritten digit samples

Challenges & Solutions
Challenge	Solution
Early training instability	Adjusted learning rate and used Adam optimizer
Similar digit confusion (e.g., 8 recognized as 3)	Added more convolutional layers to improve feature extraction
🏁 Conclusion
Key Takeaways

Learned preprocessing and normalization of image data

Gained experience training and evaluating CNN models

Achieved >99% classification accuracy

Future Work

Implement deeper CNN architecture for even stronger performance

Build a GUI / web app so users can draw digits live and test predictions
