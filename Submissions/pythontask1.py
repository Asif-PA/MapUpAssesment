# -*- coding: utf-8 -*-
"""PythonTask1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eTlEyOhU4kUAlE4OKJblWG39UEegAAhZ
"""

import pandas as pd
import numpy as np

!git clone https://github.com/Asif-PA/MapUpAssesment.git

path="/content/MapUpAssesment/dataset-1.csv"
df=pd.read_csv(path)
df.head(20)

"""# **Q1**"""

def generate_car_matrix(df):
    # Creating Pivot Table
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    # Setting diagonal values to 0
    for idx in car_matrix.index:
        car_matrix.at[idx, idx] = 0
    return car_matrix

path="/content/dataset-1.csv"
df=pd.read_csv(path)
result = generate_car_matrix(df)
print(result)

"""# **Q2**"""

def get_type_count(df):
    # Adding a new categorical column car_type
    conditions = [
        (df['car'] <= 15),
        ((df['car'] > 15) & (df['car'] <= 25)),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=choices, right=False)
    # Calculate the count
    type_count = df['car_type'].value_counts().to_dict()
    # Sorting the dictionary
    type_count = dict(sorted(type_count.items()))
    return type_count


path="/content/dataset-1.csv"
df=pd.read_csv(path)
result = get_type_count(df)
print(result)

"""# **Q3**"""

def get_bus_indexes(df):
    # Calculate the mean
    bus_mean = df['bus'].mean()
    # finding index
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()
    # Sorting
    bus_indexes.sort()
    return bus_indexes


path="/content/dataset-1.csv"
df=pd.read_csv(path)
result = get_bus_indexes(df)
print(result)

"""# **Q4**"""

def filter_routes(df):
    # Group by the 'route' and taking truck mean
    route_avg_truck = df.groupby('route')['truck'].mean()
    # Filtering routes
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    # Sorting
    selected_routes.sort()
    return selected_routes

path="/content/dataset-1.csv"
df=pd.read_csv(path)
result = filter_routes(df)
print(result)

"""# **Q5**"""

def multiply_matrix(input_df):

    # Create a copy
    modified_df = input_df.copy()
    # Apply the logic
    modified_df = modified_df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    modified_df = modified_df.round(1)
    return modified_df


result = generate_car_matrix(df)
modified_result = multiply_matrix(result)
print(modified_result)

url="/content/dataset-2.csv"
df1=pd.read_csv(url)
df1.head()