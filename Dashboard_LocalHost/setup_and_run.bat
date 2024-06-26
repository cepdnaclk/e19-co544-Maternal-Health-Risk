@echo off

REM Upgrade pip (optional, depending on your needs)
python -m pip install --upgrade pip

REM Install required dependencies from requirements.txt
pip install -r requirements.txt

REM Install missing packages individually (if any)
pip install joblib==1.4.2 pandas==2.1.0 scikit-learn==1.3.2 numpy==1.25.0 streamlit==1.36.0 mlflow

REM Start MLflow UI in a new Command Prompt window and activate the virtual environment there
start cmd /k "mlflow ui"

REM Wait a few seconds to ensure MLflow UI starts before running Streamlit
timeout /t 10 /nobreak > nul

REM Run the Streamlit app in the current Command Prompt window
streamlit run app.py
