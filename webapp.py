import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('churn_model.pkl')

# Title of the app
st.title('Bank Customer Churn Prediction')

# Input features from the user
st.header('Enter customer details:')

# Collecting inputs (with tenure feature added)
country = st.selectbox('Country', options=[0, 1, 2], format_func=lambda x: f'Country {x}')
age = st.number_input('Age', min_value=18, max_value=100, value=30)
tenure = st.number_input('Tenure (Years)', min_value=0, max_value=10, value=5)  # Add the tenure feature
balance = st.number_input('Balance', min_value=0.0, value=50000.0)
gender = st.selectbox('Gender', ('Male', 'Female'))
gender_value = 1 if gender == 'Male' else 0  # Convert gender to numeric
active_member = st.selectbox('Active Member', (1, 0))  # 1 for active, 0 for inactive
estimated_salary = st.number_input('Estimated Salary', min_value=0.0, value=50000.0)

# When the "Predict" button is clicked
if st.button('Predict'):
    # Prepare the feature vector based on inputs (with country instead of credit score)
    features = np.array([[country, gender_value, age, tenure, balance, active_member, estimated_salary]])

    # Make prediction
    prediction = model.predict(features)

    # Display the result
    if prediction[0] == 1:
        st.write('The customer is likely to churn.')
    else:
        st.write('The customer is not likely to churn.')

