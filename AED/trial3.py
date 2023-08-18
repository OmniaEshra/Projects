#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV file
data = pd.read_csv('us_international_air_traffic_data.csv')

# Pre-processing: Handling missing values
data = data.dropna()

# Pre-processing: Encoding categorical features (if any)
categorical_columns = ['Origin', 'Destination']
data_encoded = pd.get_dummies(data, columns=categorical_columns)

# Pre-processing: Scaling numerical features (if any)
numerical_columns = ['Passengers', 'Seats', 'Flights']
data_encoded[numerical_columns] = (data_encoded[numerical_columns] - data_encoded[numerical_columns].mean()) / data_encoded[numerical_columns].std()

# Visualization: Histograms for numerical columns
for column in numerical_columns:
    plt.hist(data_encoded[column])
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# Visualization: Box plots for numerical columns
for column in numerical_columns:
    sns.boxplot(data_encoded[column])
    plt.xlabel(column)
    plt.show()

# Visualization: Scatter plots for numerical columns
sns.scatterplot(data=data_encoded, x='Passengers', y='Flights')
plt.xlabel('Passengers')
plt.ylabel('Flights')
plt.show()


# In[ ]:




