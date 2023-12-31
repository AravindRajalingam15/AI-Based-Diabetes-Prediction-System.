# -*- coding: utf-8 -*-..
"""diabetes_ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1whYV9asjIiDyU0Fvv_TfOgutjOfYZiP2

IMPORTING DATASET

READING THE DATAS IN THE CSV FILE
"""

from google.colab import files
uploaded = files.upload()

import io
df = pd.read_csv(io.BytesIO(uploaded['diabetes.csv']))
print(df)

"""PRINTING THE HEADER ELEMENTS"""

print(df.head())

"""PRINTING THE BOTTOM ELEMENTS"""

print(df.tail())

"""PRINTING THE DATATYPES/INFO"""

df.info()

""" CODE FOR DIABETES PREDICTION SYSTEM"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the diabetes dataset (you can replace this with your dataset)
diabetes_data = pd.read_csv("diabetes.csv")

# Define features (X) and target variable (y)
X = diabetes_data.drop(columns=['Outcome'])  # Features
y = diabetes_data['Outcome']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Now you can use the trained model to make predictions for new data
# For example:
# new_data = [[sample_feature1, sample_feature2, ..., sample_featureN]]
# prediction = model.predict(new_data)

"""HISTOGRAM"""

df.hist()

"""SCATTER PLOT"""

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(df['Glucose'], df['BMI'], c=df['Outcome'], cmap='coolwarm')
plt.xlabel('Glucose')
plt.ylabel('BMI')
plt.title('Scatter Plot: Glucose vs. BMI')
plt.colorbar(label='Outcome')
plt.show()

"""PIE CHART/ DISTRIBUTION CHART"""

plt.figure(figsize=(6, 6))
outcome_counts = df['Outcome'].value_counts()
plt.pie(outcome_counts, labels=outcome_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'orange'])
plt.title('Pie Chart: Outcome Distribution')
plt.show()

"""BAR GRAPH"""

plt.figure(figsize=(6, 6))
outcome_counts = df['Outcome'].value_counts()
plt.bar(outcome_counts.index, outcome_counts.values, color=['skyblue', 'orange'])
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.title('Bar Graph: Outcome Counts')
plt.xticks(outcome_counts.index, ['No Diabetes', 'Diabetes'])
plt.show()
