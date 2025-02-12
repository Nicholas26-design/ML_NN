
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
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    # Drop column: 'full_name' because it's a non numeric ID.
    df = df.drop(columns=['full_name'])
    df['cluster'] = kmeans.fit_predict(df)
    centroids = kmeans.cluster_centers_
    inertia = kmeans.inertia_  # Sum of squared distances of samples to their closest cluster center
    silhouette_avg = silhouette_score(df.drop(columns=['cluster']), df['cluster'])
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
