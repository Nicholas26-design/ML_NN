# Pipeline Overview

This document provides a high-level overview of the machine learning pipeline, describing the purpose of each step and the order in which they are executed. The pipeline is automated and orchestrated by `main.py`.

## Pipeline Steps

1. **Install Code Packages**  
   - Purpose: Ensure all required dependencies are installed.  
   - Script: `requirements.py`  

2. **Install Datasets**  
   - Purpose: Download and prepare the datasets needed for the pipeline.  
   - Script: `install_datasets.py`  

3. **Cluster and Impute Missing Values**  
   - Purpose: Group data into clusters based on similarity and fill in missing values to create a complete dataset.  
   - Script: `clustering_missing_value_imputation.py`  

4. **Encode Categorical Features**  
   - Purpose: Convert categorical features into machine-readable formats for model training.  
   - Script: `encoding.py`  

5. **AdClicks Analysis**  
   - Purpose: Predict whether a user will click on an ad using classification algorithms.  
   - Script: `AdClicks.py`  

## Classification Algorithms

The AdClicks analysis step uses the following classification algorithms:

- **Logistic Regression**: Suitable for binary classification problems. Uses a sigmoid function to predict probabilities.  
- **Support Vector Machines (SVM)**: Identifies support vectors closest to the decision boundary (hyperplane).  
- **Decision Trees**: Splits data using if-else conditions at each branch.  
- **Random Forest**: An ensemble method combining multiple decision trees for improved accuracy.