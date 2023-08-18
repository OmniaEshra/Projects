#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path, file_type):
    if file_type == 'csv':
        data = pd.read_csv(file_path)
    elif file_type == 'excel':
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type.")
    return data

def handle_missing_values(data):
    data.fillna(np.mean(), inplace=True)

def preprocess_data(data):
    numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = identify_categorical_features(data)

# Impute missing values
    imputer = SimpleImputer(strategy='mean')
    data[numerical_features] = imputer.fit_transform(data[numerical_features])
    handle_missing_values(data)

# One-hot encode categorical features
    data = pd.get_dummies(data, columns=[feature for feature, _ in categorical_features])
    scaler = StandardScaler()
    data[numerical_features] = scaler.fit_transform(data[numerical_features])

    return data

def identify_categorical_features(data):
    categorical_features = data.select_dtypes(include=['object']).columns
    features = []

    for feature in categorical_features:
        unique_values = data[feature].nunique()
        if unique_values == 2:
            features.append((feature, 'binary'))
        else:
            features.append((feature, 'categorical'))

    return features

def create_scatter_plot(data, feature):
    plt.figure(figsize=(10, 7))
    plt.scatter(data[feature], data['Total'])
    plt.xlabel(feature)
    plt.ylabel('Total')
    plt.title(f'Scatter Plot of {feature}')
    plt.show()

def create_pie_plot(data, feature):
    feature_counts = data[feature].value_counts()
    plt.figure(figsize=(10, 7))
    plt.pie(feature_counts, labels=feature_counts.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title(f'Pie Plot of {feature}')
    plt.show()

def create_bar_plot(data, feature):
    plt.figure(figsize=(10, 7))
    sns.countplot(data=data, x=feature)
    plt.title(f'Bar Plot of {feature}')
    plt.xticks


# In[ ]:




