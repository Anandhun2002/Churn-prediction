import streamlit as st
import pandas as pd
import pickle

# Load the model and preprocessor
with open('best_knn_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('preprocessor.pkl', 'rb') as f: 
    pre = pickle.load(f)

# App title and header
st.title("Customer Churn Prediction App")
st.header("Enter Customer Information")

# User input fields
gender = st.selectbox("Gender", ['Male', 'Female'])
InternetService = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
Contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
tenure = st.number_input("Tenure (in months)", min_value=0, max_value=100, value=1)
MonthlyCharges = st.number_input("Monthly Charges", min_value=0, max_value=200, value=50)
TotalCharges = st.number_input("Total Charges", min_value=0, max_value=10000, value=0)

# Button for prediction
submit = st.button('Submit')

if submit:
    # Prepare the input data
    data = {
        'gender': [gender],
        'InternetService': [InternetService],
        'Contract': [Contract],
        'tenure': [tenure],
        'MonthlyCharges': [MonthlyCharges],
        'TotalCharges': [TotalCharges],
    }
    data_df = pd.DataFrame(data)

    # Apply preprocessing
    data_processed = pre.transform(data_df)

    # Make a prediction
    prediction = model.predict(data_processed)

    # Display result
    if prediction[0] == 0:
        st.success("This customer is likely to stay.")
    else:
        st.error("This customer is likely to churn.")
