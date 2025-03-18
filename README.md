# Customer Churn Prediction

## Overview
This project is a **Customer Churn Prediction App** that uses machine learning to predict whether a customer is likely to churn based on various attributes such as **gender, internet service type, contract type, tenure, monthly charges, and total charges**.

The model is deployed as a **Streamlit web application**, allowing users to input customer information and get real-time predictions.

## Features
- **Machine Learning Model**: Uses a trained K-Nearest Neighbors (KNN) classifier.
- **Data Preprocessing**: Includes transformations applied to user inputs before prediction.
- **User-Friendly Interface**: Built with **Streamlit** for easy interaction.
- **Real-Time Predictions**: Users can input customer details and instantly get predictions on whether the customer will churn.

## Files
- **`app.py`** - Streamlit app that loads the trained model and preprocessor, collects user inputs, and makes predictions.
- **`best_knn_model.pkl`** - The pre-trained KNN model used for predictions.
- **`preprocessor.pkl`** - The preprocessing pipeline used to transform input data before feeding it into the model.
- **`mini project churn_prediction.ipynb`** - Jupyter Notebook containing the machine learning workflow, including data processing, model training, and evaluation.



## Model & Data Processing
- The dataset used for training contains customer attributes.
- Features are preprocessed using a pipeline saved in `preprocessor.pkl`.
- A **K-Nearest Neighbors (KNN)** model is used for classification.


