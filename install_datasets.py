import kagglehub

# Download latest version
path = kagglehub.dataset_download("bricevergnou/spotify-recommendation", download_dir="../datasets")

print("Path to dataset files:", path)

# Download latest version
path = kagglehub.dataset_download("marius2303/ad-click-prediction-dataset", download_dir="../datasets")

print("Path to dataset files:", path)

# Download latest version
path = kagglehub.dataset_download("dorianlazar/medium-articles-dataset", download_dir="../datasets")

print("Path to dataset files:", path)