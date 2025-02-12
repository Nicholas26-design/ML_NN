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

# Loaded variable 'df' from URI: c:\Users\NicholasKenney\PycharmProjects\Key2_Blog\EncodedData.csv
import pandas as pd
df = pd.read_csv(r'c:\\Users\\NicholasKenney\\PycharmProjects\\Key2_Blog\\EncodedData.csv')