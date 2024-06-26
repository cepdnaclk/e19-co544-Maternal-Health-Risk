import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the model and scaler
model_path = "rf.pkl"
scaler_path = "scaler.pkl"
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Set up the Streamlit app
st.title('Maternal Health Risk Prediction')
image_path = "Mathealth.jpg"
st.image(image_path, width=400)
# Input features from the user with validation
st.sidebar.header('Input Parameters')
age = st.sidebar.number_input('Age', min_value=10, max_value=100, value=25)
systolic_bp = st.sidebar.number_input('Systolic Blood Pressure (mm Hg)', min_value=80, max_value=200, value=120)
bs = st.sidebar.number_input('Blood Sugar Level (mmol/l)', min_value=0.00, max_value=20.00, value=5.00, format="%.2f")
body_temp = st.sidebar.number_input('Body Temperature (°F)', min_value=90.0, max_value=120.0, value=98.0, format="%.1f")
# Validate inputs
if age < 10 or age > 100:
    st.sidebar.error("Age must be between 10 and 100.")
if systolic_bp < 80 or systolic_bp > 200:
    st.sidebar.error("Systolic Blood Pressure must be between 80 and 200 mm Hg.")
if bs < 0.00 or bs > 20.00:
    st.sidebar.error("Blood Sugar Level must be between 0.00 and 20.00 mmol/L.")
if body_temp < 90.0 or body_temp > 120.0:
    st.sidebar.error("Body Temperature must be between 90.0 and 120.0 °F.")

# Feature names (matching those used during training)
feature_names = ['Age', 'SystolicBP', 'BS', 'BodyTemp']
input_data = pd.DataFrame([[age, systolic_bp, bs, body_temp]], columns=feature_names)

# Display input data
st.subheader('User Input Parameters')
st.write(input_data)

# Predict button
if st.button('Predict'):
    # Check if any validation errors exist
    validation_errors = False
    if age < 10 or age > 100 or systolic_bp < 80 or systolic_bp > 200 or bs < 0.00 or bs > 20.00 or body_temp < 90.0 or body_temp > 120.0:
        validation_errors = True

    if not validation_errors:
        # Apply the same scaling to input data
        input_data_scaled = scaler.transform(input_data)
        #st.write(input_data_scaled)
        # Make the prediction
        try:
            prediction = model.predict(input_data_scaled)
            risk_mapping = {0: 'low risk', 1: 'mid risk', 2: 'high risk'}
            risk_level = risk_mapping[prediction[0]]
            # Display the prediction
            st.subheader('Prediction')
            st.write(f'Predicted Risk Level: {risk_level.capitalize()}')
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
    else:
        st.error("Please correct the input values to meet the validation criteria.")

# To run the app, save this script as `app.py` and use the following command:
# streamlit run app.py
