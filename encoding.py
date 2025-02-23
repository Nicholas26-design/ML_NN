
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np
import os


# Load your dataset
script_dir = os.path.dirname(__file__)  # Directory of the script being run
data_path = os.path.join(script_dir, 'imputed_categorical_dataset.csv')
df = pd.read_csv(data_path)


# Data encoding function
def encode_data(df):
    # One-hot encode categorical features
    df = pd.get_dummies(df, columns=['gender', 'device_type', 'ad_position', 'browsing_history'], dtype=float)

    # Ordinal encode 'time_of_day'
    time_of_day_mapping = {"Morning": 0, "Afternoon": 1, "Evening": 2, "Night": 3}
    df['time_of_day'] = df['time_of_day'].map(time_of_day_mapping)
    return df


# Feature scaling function
def scale_features(df):

    scaler = StandardScaler()
    # Identify continuous numerical columns to scale (exclude one-hot and ordinal-encoded)
    continuous_columns = ['age_imputed']  # Adjust this list based on your dataset
    df_scaled = df.copy()
    df_scaled[continuous_columns] = scaler.fit_transform(df[continuous_columns])
    return df_scaled

# Define continuous numerical columns
continuous_columns = ['age_imputed']

# Preprocessing pipeline
# Encode data
df_encoded = encode_data(df.copy())
# Scale continuous features
df_scaled = scale_features(df_encoded)

# Output results
print("Encoded Data:")
print(df_scaled.head())
data_path = os.path.join(script_dir, 'EncodedData.csv')
df_scaled.to_csv(data_path)

