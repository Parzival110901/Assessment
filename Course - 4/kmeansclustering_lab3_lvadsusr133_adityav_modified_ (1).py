# -*- coding: utf-8 -*-
"""KMeansClustering-lab3-lvadsusr133-Adityav modified .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yZ4_ObQ4jsl6YVQtnnpbERJahinLiwNi
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.impute import SimpleImputer
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

# Step 1: Read Data
df = pd.read_csv('/content/seeds.csv')

# Step 2: Replace Missing Values
# Check for missing values
print("Missing Values Before Imputation:")
print(df.isnull().sum())

# Replace missing values with median
imputer = SimpleImputer(strategy='median')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Step 3: Remove Outliers
# Use Isolation Forest to identify outliers
outlier_detector = IsolationForest(contamination=0.05, random_state=42)
outliers = outlier_detector.fit_predict(df_imputed)

# Remove outliers
df_cleaned = df_imputed[outliers == 1]

# Step 4: Perform Exploratory Data Analysis (EDA)
# Summary Statistics
print("Summary Statistics:")
print(df_cleaned.describe())

# Visualization
sns.pairplot(df_cleaned)
plt.show()

# Step 5: Model Training and Testing
# Feature Scaling
scaler = StandardScaler()
X = scaler.fit_transform(df_cleaned)

# Splitting into training and test sets
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Fit KMeans clustering model on training set
kmeans = KMeans(random_state=42)

# Initialize list to store inertia values
inertia_values = []

# Range of clusters to test
num_clusters_range = range(1, 11)

# Calculate inertia for each number of clusters
for num_clusters in num_clusters_range:
    kmeans.set_params(n_clusters=num_clusters)
    kmeans.fit(X_train)
    inertia_values.append(kmeans.inertia_)

# Plot the Elbow Method
plt.plot(num_clusters_range, inertia_values, marker='o', linestyle='-')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.xticks(num_clusters_range)
plt.show()

# Step 6: Model Evaluation (Optional)
# Evaluate clustering using silhouette score on test set
silhouette_avg = silhouette_score(X_test, kmeans.predict(X_test))
print("Silhouette Score:", silhouette_avg)

# Step 7: Predict on Test Set
# If you have a separate test dataset, you can read it similarly to how you read the training data
# Or, you can use the existing dataset and split it into training and test sets
# Then, you can predict clusters on the test set using the trained model

# For example, if you have df_test as your test dataset
# Predict clusters on the test set
test_clusters = kmeans.predict(X_test)

# Print the predicted clusters on the test set
print("Predicted Clusters on Test Set:")
print(test_clusters)