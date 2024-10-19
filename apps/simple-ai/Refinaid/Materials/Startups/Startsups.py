# %% [markdown]
# Importing libraries for working with dataset and machine learning models

# %%
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split
import ydata_profiling
import seaborn as sns

# %% [markdown]
# Dataset from Kaggle - https://www.kaggle.com/datasets/utkarshx27/2021-startups

# %%
data = pd.read_csv('Startups_in_2021_end.csv')

# %% [markdown]
# This data is about startups from 2012 to 2021.  
# 
# The fileld unnamed:0 is the startup ID.    
# Company is the name of the startup.     
# Valuation ($B) - valuation in dollars.      
# Date Joined - the date of joining the organization.  
# Country and city are the place where a startup appears.  
# Industry - in which industry the startup was created.  
# Select Investors - list of investors

# %%
data

# %% [markdown]
# Let's look at the peculiarity of the data

# %%
ydata_profiling.ProfileReport(data)

# %% [markdown]
# To prepare the data, I need to translate text values into numbers. To do this, I need to clean up the data. Let's get rid of extra commas in the data, reduce the text to lowercase in Country and Industry fields. Let's make a dictionary of unique values

# %%
def replace_country(country):
    return country.split(',')[0]

def get_lowregiser(industry):
    return industry.lower()

def get_dict(column):
    d = {}
    for i in range(0, len(column.unique())):
        d[column.unique()[i]] = float(i)
    return d

data.drop('Unnamed: 0', axis=1, inplace=True)
data['Country'] = data['Country'].apply(replace_country)
data['Industry'] = data['Industry'].apply(get_lowregiser)
dict_country = get_dict(data['Country'])
dict_industry = get_dict(data['Industry'])

# %% [markdown]
# Let's get rid of the dollar sign in the Valuation field. We will leave only the year in the Date field. Day and month do not significantly affect the work of the model, in my opinion

# %%
def transform_valuation(valuation):
    return float(valuation.split('$')[1])

def transform_date(date):
    return int(date.split('/')[2])

def transform_country(country, dictionary):
    return dictionary[country]

def transform_industry(industry, dictionary):
    return dictionary[industry]

# %%
data['Valuation ($B)'] = data['Valuation ($B)'].apply(transform_valuation)
data['Date Joined'] = data['Date Joined'].apply(transform_date)
data['Country'] = data['Country'].apply(lambda x: transform_country(x, dict_country))
data['Industry'] = data['Industry'].apply(lambda x: transform_industry(x, dict_industry))

# %% [markdown]
# We have this dataset after transformation

# %%
data

# %% [markdown]
# I want to build classification models. I need to choose one column, which machine will predict. I choose Select Investors column. I think, that Company and City columns do not affect the final investors. Therefore, I will delete them

# %%
data.drop('Company', axis=1, inplace=True)
data.drop('City', axis=1, inplace=True)

# %% [markdown]
# Check columns for NaN 

# %%
data.isnull().sum()

# %% [markdown]
# The field Select Investors should be converted to the values 1 and 0. If the startup has more or three investors, we give the value 1. Otherwise 0. Therefore, we give the NaN value 0. The model will classify whether the startup will have more or equal to 3 investors

# %%
data['Select Investors'] = data['Select Investors'].fillna(value = '0')

# %%
def transform_target(investors):
    if len(investors.split(',')) >= 3:
           return 1
    else:
           return 0

data['Select Investors'] = data['Select Investors'].apply(transform_target)

# %% [markdown]
# Final dataset

# %%
data

# %% [markdown]
# Let's look at the correlation table

# %%
corr = data.corr()
corr.style.background_gradient(cmap='coolwarm')

# %% [markdown]
# Fileds Country, Industry and Valuation affect target(Select Investors). I will use this columns for machine learning and delete column Date, because it does not affect target

# %%
X = data.drop(['Select Investors', 'Date Joined'], axis = 1)
Y = data['Select Investors']

# %% [markdown]
# Divide datsaet in the ratio 70% for learning and 30% for test

# %%
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 42)

# %% [markdown]
# Create DecisionTree model. Accuracy is 0.79

# %%
tree = DecisionTreeClassifier(max_depth = 10)
tree_simple = tree.fit(X_train, Y_train)
predictions = tree_simple.predict(X_test)
print(classification_report(Y_test, predictions))

# %% [markdown]
# Create RandomForest model. Accuracy is 0.82

# %%
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 42)
classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_test)
print(classification_report(Y_test, y_pred))

# %% [markdown]
# Create LogisticRegression model. Accuracy is 0.85

# %%
logisticRegression = LogisticRegression(random_state = 42)
logisticRegression.fit(X_train, Y_train)
y_pred = logisticRegression.predict(X_test)
print(classification_report(Y_test, y_pred))

# %%



