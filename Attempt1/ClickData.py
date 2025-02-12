
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv(r'C:\Users\NicholasKenney\PycharmProjects\Key2_Blog\datasets\ad-click-prediction-dataset\versions\5\ad_click_dataset.csv')



# Data cleaning function
def clean_data(df):
    # Fill missing values
    df = df.fillna({
        'age': df['age'].mean(),  # Mean for numerical column
        'time_of_day': df['time_of_day'].mode()[0]  # Mode for categorical column with ordinal meaning
    })
    return df


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
    continuous_columns = ['age']  # Adjust this list based on your dataset
    df_scaled = df.copy()
    df_scaled[continuous_columns] = scaler.fit_transform(df[continuous_columns])
    return df_scaled


# K-Means clustering function
def perform_clustering(df, n_clusters=3):
    # Drop non-numeric or categorical columns that will not be used in clustering
    df_features = df.drop(columns=['full_name'])

    # Separate categorical columns (e.g., one-hot encoded features)
    categorical_cols = df_features.select_dtypes(include=['object', 'category']).columns
    numerical_cols = df_features.select_dtypes(include=['float64', 'int64']).columns

    # Impute missing numerical values with the mean
    imputer_num = SimpleImputer(strategy='mean')
    df_features[numerical_cols] = imputer_num.fit_transform(df_features[numerical_cols])

    # Perform K-Means clustering on numerical features
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df_features['cluster'] = kmeans.fit_predict(df_features[numerical_cols])

    # Impute categorical features based on clusters
    for col in categorical_cols:
        # For each categorical column, impute missing values using the mode of the cluster
        for cluster in range(n_clusters):
            # Find the rows in the current cluster
            cluster_rows = df_features[df_features['cluster'] == cluster]

            # For each missing value in the column, impute with the mode of that cluster
            mode_value = cluster_rows[col].mode()[0]  # Mode for the cluster
            df.loc[(df[col].isna()) & (df['cluster'] == cluster), col] = mode_value

    # Calculate metrics
    centroids = kmeans.cluster_centers_
    inertia = kmeans.inertia_  # Sum of squared distances of samples to their closest cluster center
    silhouette_avg = silhouette_score(df_features[numerical_cols], df_features['cluster'])

    return df, centroids, inertia, silhouette_avg



# Define continuous numerical columns
continuous_columns = ['age']

# Preprocessing pipeline
df_clean = clean_data(df.copy())
df_encoded = encode_data(df_clean)
# Scale continuous features
df_scaled = scale_features(df_encoded)
# # Perform K-Means clustering
df_clustered, centroids, inertia, silhouette_avg = perform_clustering(df_scaled, n_clusters=3)



# Verification
# df_scaled.to_csv('C:\\Users\\NicholasKenney\\PycharmProjects\\Key2_Blog\\output3.csv')

# # Perform K-Means clustering
# df_clustered, centroids, inertia, silhouette_avg = perform_clustering(df_scaled, n_clusters=3)
#
# # Output results
print("Clustered Data:")
print(df_clustered.head())
df_clustered.to_csv('C:\\Users\\NicholasKenney\\PycharmProjects\\Key2_Blog\\output3.csv')

# print("\nCluster Centroids:")
# print(centroids)
# print(f"\nInertia: {inertia}")
# print(f"Silhouette Score: {silhouette_avg}")
