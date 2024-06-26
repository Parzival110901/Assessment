# -*- coding: utf-8 -*-
"""LVAD-SUSR133-Aditya-IA1-LinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12cua1yXRj0UdxIt-ekLBm_MrYHRXkxEQ

# New section
"""

#Linear Regression

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



# Function for EDA, Outlier Detection, and Linear Regression

def perform_linear_regression(dataset_path):
    # Load the dataset
    df = pd.read_csv(dataset_path)

    # Fill null values
    df.fillna(method='ffill', inplace=True)

    # Convert categorical variables into dummy/indicator variables (one-hot encoding)
    df = pd.get_dummies(df, drop_first=True)  # Drop first to avoid multicollinearity

    # Exploratory Data Analysis and data cleaning
    print("===== Exploratory Data Analysis =====")
    print("Dataset Shape:", df.shape)
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    print("\nData Types:")
    print(df.dtypes)
    print("\nSummary Statistics:")
    print(df.describe())
    print("\nMissing Values:") #missing values handle
    print(df.isnull().sum())

    # Outlier Detection
    print("\n===== Outlier Detection =====")
    # Detect outliers using IQR method
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)
    print("Number of outliers detected:", outliers.sum())

    # Data Visualization
    print("\n===== Data Visualization =====")
    # Pairplot for numerical variables without outliers
    sns.pairplot(df[~outliers])
    plt.show()

    # Correlation matrix
    print("===== Correlation Analysis =====")
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

    # Model Building and Evaluation
    print("===== Model Building and Evaluation =====")
    # target variable
    X = df.drop('charges', axis=1)
    y = df['charges']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Linear Regression
    print("\nLinear Regression Model")
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    y_pred = lin_reg.predict(X_test)

    # Model evaluation
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error:", mse)


linear_regression_dataset_path = "/content/expenses.csv"
perform_linear_regression(linear_regression_dataset_path)