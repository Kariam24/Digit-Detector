# Digit-Detector

By: Kariam Rodriguez, Yanni Pierre, Izze Lino, Sebastian Barrera
Course: CAP 4630

📌 Overview

This project uses a neural network to recognize handwritten digits (0–9) from the MNIST dataset. The model learns patterns from thousands of labeled digit images and predicts the correct number when given a new handwritten input. Applications include digital form processing, bank check readers, and postal mail sorting.

🎯 Objectives

Train a model capable of classifying handwritten digits with high accuracy

Understand neural network training and evaluation

Build a simple interactive interface where users can draw and test digits

🧠 Model Details

Dataset: MNIST (70,000 grayscale digit images, 28×28 px)

Framework: TensorFlow / Keras

Architecture: Dense layers + Batch Normalization + Dropout

Dense(30, ReLU)

Dense(10, Softmax)

Loss Function: Sparse Categorical Crossentropy

Optimizer: Adam

Training Results

Training Accuracy: 99.39%

Validation Accuracy: 99.51%
(Shown in slides) 

AI Digit Detector Project

⚙️ Methodology
Data Input → Preprocessing → Model Training → Evaluation → Prediction


Normalized pixel values (0–1)

Trained for 10 epochs

Evaluated performance with accuracy metrics

📈 Results & Insights

Strong performance and generalization

Small gap between training and validation → minimal overfitting

Consistently predicts unseen handwritten digit images

Challenges

Difficult to improve beyond ~97% using basic CNN

More computing power needed for more complex architectures
