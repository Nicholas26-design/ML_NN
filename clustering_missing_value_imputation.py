

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Load your dataset
data = pd.read_csv(r'C:\\Users\\NicholasKenney\\PycharmProjects\\Key2_Blog\\datasets\\ad-click-prediction-dataset\\versions\\5\\ad_click_dataset.csv')


# Step 1: Select relevant features for clustering
features = ['age', 'gender', 'device_type', 'ad_position', 'browsing_history', 'time_of_day']
data_subset = data[features]

# Step 2: Preprocess data
categorical_features = ['gender', 'device_type', 'ad_position', 'browsing_history', 'time_of_day']
numerical_features = ['age']

# Handle missing values in categorical features
encoders = {col: LabelEncoder() for col in categorical_features}
for col in categorical_features:
    data_subset[col] = data_subset[col].fillna("Missing")  # Fill missing values with "Missing"
    data_subset[col] = encoders[col].fit_transform(data_subset[col])

# Scale numerical features
scaler = StandardScaler()
data_subset[numerical_features] = scaler.fit_transform(data_subset[numerical_features].fillna(-1))  # Fill missing with -1 temporarily

# Step 3: Apply K-Means Clustering
kmeans = KMeans(n_clusters=5, random_state=42)  # Adjust the number of clusters as needed
data_subset['cluster'] = kmeans.fit_predict(data_subset)

# Step 4: Impute missing 'age' values based on cluster means
data['cluster'] = data_subset['cluster']  # Add cluster info back to the original data
cluster_means = data.groupby('cluster')['age'].transform('mean')  # Get cluster means for 'age'

# Replace missing 'age' values with cluster means
data['age_imputed'] = data['age']
data['age_imputed'] = data['age_imputed'].fillna(cluster_means)
# Round up column 'age_imputed'
data[['age_imputed']] = np.ceil(data[['age_imputed']])

# # Save the results to a new file
# data.to_csv("imputed_dataset.csv", index=False)
#
# # Optional: Preview results
# print(data[['age', 'age_imputed', 'cluster']].head(10))


# Function to impute missing categorical values based on cluster modes
def impute_categorical_cluster_mode(data, cluster_col, cat_col):
    """Impute missing values in a categorical column using the mode within each cluster."""
    # Calculate cluster-wise modes
    cluster_modes = (
        data.groupby(cluster_col)[cat_col]
        .apply(lambda x: x.mode().iloc[0] if not x.mode().empty else "Unknown")
    )

    # Replace missing values with the cluster mode
    return data.apply(
        lambda row: cluster_modes[row[cluster_col]]
        if pd.isnull(row[cat_col]) or row[cat_col] == "Missing"
        else row[cat_col],
        axis=1,
    )


# Apply the function for all categorical columns
for col in categorical_features:
    data[col] = impute_categorical_cluster_mode(data, "cluster", col)

# Drop a specific column
data = data.drop(columns=['age'])

# Save the updated dataset with categorical imputation
data.to_csv("imputed_categorical_dataset.csv", index=False)

# Preview results
print(data.head(10))

