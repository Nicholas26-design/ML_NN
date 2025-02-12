import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(filename='install_errors.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def install_requirements(requirements_file):
    try:
        with open(requirements_file, 'r') as file:
            packages = file.readlines()
            packages = [pkg.strip() for pkg in packages]

            for package in packages:
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                    print(f"Successfully installed {package}")
                except subprocess.CalledProcessError as e:
                    logging.error(f"Failed to install {package}. Error: {e}")
                except Exception as e:
                    logging.error(f"An unexpected error occurred while installing {package}. Error: {e}")

        print("All packages processed.")
    except FileNotFoundError:
        logging.error(f"The file {requirements_file} was not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


# Specify the path to the requirements.txt file
requirements_file = 'requirements.txt'

# Call the function to install packages
install_requirements(requirements_file)