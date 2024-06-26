# Maternal Health Risk Prediction

This project predicts maternal health risk based on various features. The project includes a Streamlit dashboard and utilizes MLflow for tracking and managing machine learning experiments.

## Project Structure

- `app.py`: The main Streamlit application file that contains the code for the dashboard.
- `requirements.txt`: A file listing all the dependencies required to run the application.
- `setup_and_run.bat`: A batch script for Windows to set up the virtual environment, install dependencies, start the MLflow UI, and run the Streamlit app.
- `setup_and_run.sh`: A shell script for Unix-like systems (Linux, macOS) to perform the same setup and run tasks as `setup_and_run.bat`.
- `feature_config.yaml`: A configuration file for documenting the features and parameters of the dataset.
- `rf.pkl`: A pickled file containing the trained Random Forest model.
- `scaler.pkl`: A pickled file containing the scaler used for feature scaling.
- `mypic.jpg`: The image to display in the dashboard.

## Setup and Usage

### Prerequisites

- Python 3.7 or higher
- Git (optional, for version control)
- A terminal or Command Prompt

### Installation and Running the Application

#### Windows

1. Clone the repository or download the files to your local machine.
    ```sh
    git clone https://github.com/cepdnaclk/e19-co544-Maternal-Health-Risk
    cd Dashboard_LocalHost
    ```

2. Run the `setup_and_run.bat` script.
    ```sh
    # Step 1: Create virtual environment
    pip install virtualenv 
    python -m virtualenv myenv

    # Step 2: Activate virtual environment
    myenv\Scripts\activate.bat

    # Step 3: Run setup and run script
    setup_and_run.bat
    ```

    if needed:
    ```sh
    pip install setuptools
    ```

    If you get an execution policy error, execute this command first in Powershell:
        ```sh
        Set-ExecutionPolicy -Scope CurrentUser Unrestricted
        ```

    If you have finished working, then change the policy:
        ```sh
        Set-ExecutionPolicy -Scope CurrentUser Restricted
        ```

   This script will:
   - Create a virtual environment.
   - Activate the virtual environment.
   - Install the required dependencies.
   - Start the MLflow UI.
   - Run the Streamlit application.

#### Unix-like Systems (Linux, macOS)

1. Clone the repository or download the files to your local machine.
    ```sh
    git clone https://github.com/cepdnaclk/e19-co544-Maternal-Health-Risk
    cd Dashboard_LocalHost
    ```

2. Make the `setup_and_run.sh` script executable.
    ```sh
    chmod +x setup_and_run.sh
    ```

3. Run the `setup_and_run.sh` script.
    # Step 1: Create virtual environment
    python3 -m venv myenv

    # Step 2: Activate virtual environment
    source myenv/bin/activate

    # Step 3: Run setup and run script
    ./setup_and_run.sh


   This script will:
   - Create a virtual environment.
   - Activate the virtual environment.
   - Install the required dependencies.
   - Start the MLflow UI.
   - Run the Streamlit application.

## Usage

- After running the setup script, the Streamlit app will be available at `http://localhost:8501`.
- The MLflow UI will be available at the URL provided by the script (usually `http://localhost:5000`).

## Dependencies

All required dependencies are listed in the `requirements.txt` file. The main dependencies include:
- `streamlit`
- `pandas`
- `scikit-learn`
- `numpy`
- `mlflow`

## Running Tests

To run tests, use the following scripts depending on your operating system:
### Windows
python run_tests.bat

### Unix-like Systems (Linux, macOS)
python run_tests.sh


## Acknowledgements

- The dataset used in this project is provided by [Marzia Ahmed - UCI](https://archive.ics.uci.edu/dataset/863/maternal+health+risk).
- [Kaggle details](https://www.kaggle.com/datasets/csafrit2/maternal-health-risk-data/data)

## Contact

For any questions or feedback, please contact:
- [Achsuthan](mailto:e19007@eng.pdn.ac.lk)
- [Delini](mailto:e19069@eng.pdn.ac.lk)
- [Harnan](mailto:e19134@eng.pdn.ac.lk)
- [Hamshica](mailto:e19244@eng.pdn.ac.lk)
- [Thevambikai](mailto:e19494@eng.pdn.ac.lk)
- [GitHub Issues](https://github.com/cepdnaclk/e19-co544-Maternal-Health-Risk/issues)
