Steps:

1. Install code packages via requirements script
2. Install datasets via install_datasets script
3. Run the clustering_missing_value_imputation script. It groups data into clusters based on how similar the data points are. The original data isn't thorough so it needs to be filled in so that there's a complete dataset.
4. Run the encoding script. Categorical features can't be read by machines so this changes that.
5. Final step is to run the AdClicks script.


    Classification: discrete output. Outcomes must be small and finite. The value wouldn't be continuous, like 1.7. Predicting if a user clicks on an ad.
		○ Logistic regression: often used for binary problems. Sigmoid function.
		○ Support Vector: support vectors are the data points closest to the decision boundary (hyperplane).
		○ Decision Tree: Each branch is if-else.
    Random Forest is a collection of decision trees.