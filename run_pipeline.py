import subprocess

def run_script(script_name):
    """Runs a script and handles errors."""
    print(f"Running {script_name}...")
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
        raise RuntimeError(f"Script {script_name} failed.")
    else:
        print(f"Successfully ran {script_name}: {result.stdout}")

def install_requirements():
    run_script("install_requirements.py")

def preprocess_data():
    run_script("src/data_preprocessing/clustering_missing_value_imputation.py")
    run_script("src/data_preprocessing/encoding.py")

def analyze_data():
    run_script("src/analysis/AdClicks.py")
    run_script("src/analysis/ClickData.py")
    run_script("src/analysis/Clicks.py")

if __name__ == "__main__":
    install_requirements()
    preprocess_data()
    analyze_data()
    print("Pipeline execution completed.")
