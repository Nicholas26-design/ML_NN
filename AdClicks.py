"""
This is an Ad Click Prediction Dataset. This will address click-through on our ads/articles.
The data has gone through the following feature engineering process:
1. Missing data has been imputed through k-means clustering
2. Nominal features have been scaled
3. Categorical features have been encoded.
"""

"""
Model Objectives:
Given the information at hand, who is most likely to click on the ad?
What ads are most effective?
"""

import pandas as pd
import os

# Load your dataset
script_dir = os.path.dirname(__file__)  # Directory of the script being run
data_path = os.path.join(script_dir, '../datasets/EncodedData.csv')
df = pd.read_csv(data_path)
print(df.head(10))