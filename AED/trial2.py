#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

class AutomatedEDA:
    def __init__(self, data):
        self.data = data

    def load_data(self, file_path, file_type):
        if file_type == 'csv':
            self.data = pd.read_csv(file_path)
        elif file_type == 'excel':
            self.data = pd.read_excel(file_path)
        elif file_type == 'sql':
            pass

    def preprocess_data(self):
        self.data.fillna(0, inplace=True)
        # Encode categorical features
        categorical_cols = self.data.select_dtypes(include=['object']).columns
        self.data[categorical_cols] = self.data[categorical_cols].astype('category')
        self.data[categorical_cols] = self.data[categorical_cols].apply(lambda x: x.cat.codes)
        # Scale numerical features
        numerical_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
        self.data[numerical_cols] = (self.data[numerical_cols] - self.data[numerical_cols].mean()) / self.data[numerical_cols].std()

    def visualize_data(self):
        # Generate visualization dashboard for each column type
        for column in self.data.columns:
            if self.data[column].dtype.name == 'category':
                fig = px.histogram(self.data, x=column)
                fig.show()
            elif self.data[column].dtype.name in ['float64', 'int64']:
                fig = px.box(self.data, y=column)
                fig.show()
            else:
                pass

            if __name__ == '__main__':
                eda = AutomatedEDA(None)
                eda.load_data('path_to_data_file.csv', 'csv')
                eda.preprocess_data()
                eda.visualize_data()


# In[ ]:




