# Digit-Detector

By: Kariam Rodriguez, Yanni Pierre, Izze Lino, Sebastian Barrera
Course: CAP 4630

Overview

This project builds and trains a machine learning model that recognizes handwritten digits (0–9) using the MNIST dataset. The model uses deep learning to analyze grayscale images and predict which digit was written. This type of technology powers systems like check readers, postal sorting machines, and digitized forms.

Objectives

Train an AI model to classify handwritten digits accurately

Understand how neural networks process image data

Develop a simple interface where users can draw a digit and receive a prediction

Model & Tools

Dataset: MNIST (70,000 samples, 28×28 grayscale images)

Framework: TensorFlow / Keras

Architecture: Dense layers with Batch Normalization & Dropout
Dense(30, ReLU), Dense(10, Softmax)

Optimizer: Adam

Loss: Sparse Categorical Crossentropy

Training Results

Accuracy: 99.39% training, 99.51% validation
(Shown in slides) 

AI Digit Detector Project

Method
Data Input → Preprocessing → Model Training → Evaluation → Prediction Output


Normalized data (0–1)

Trained for 10 epochs

Evaluated accuracy and validation loss

Results

High accuracy on unseen handwritten digits

Minimal overfitting

Model performs strong with a basic structure

Challenges

Hard to improve beyond 97% using simple CNN

More computation needed for advanced accuracy
