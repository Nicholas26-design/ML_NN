import subprocess


# See the STEPS markdown for a detailed explanation on why the given order is what it is.

def run_script(script_name):
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
    else:
        print(f"Successfully ran {script_name}: {result.stdout}")


if __name__ == "__main__":
    run_script('install_requirements.py')
    run_script('install_datasets.py')
    run_script('clustering_missing_value_imputation.py')
# The script above groups data into clusters based on how similar the data points are.
# The original data isn't filled out so it needs to be filled in so that there's a complete dataset.
    run_script('encoding.py')  # Categorical features can't be read by machines so this changes that.
    run_script('AdClicks.py')

