#!/bin/bash

# Upgrade pip (optional, depending on your needs)
python -m pip install --upgrade pip

# Install required dependencies from requirements.txt
pip install -r requirements.txt

# Install missing packages individually (if any)
pip install joblib==1.4.2 pandas==2.1.0 scikit-learn==1.3.2 numpy==1.25.0 streamlit==1.36.0 mlflow

# Start MLflow UI in a new terminal session (background process)
mlflow ui &

# Wait a few seconds to ensure MLflow UI starts before running Streamlit
sleep 10

# Run the Streamlit app in the current terminal session
streamlit run app.py
