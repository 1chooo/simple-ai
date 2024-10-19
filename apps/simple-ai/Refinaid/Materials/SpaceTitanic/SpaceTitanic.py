#Import necessary libraries
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split
import ydata_profiling
import seaborn as sns

# https://www.kaggle.com/competitions/spaceship-titanic/data - dataset Spaceship Titanic.

#PassengerId - id of everybody passenger
#HomePlanet - passenger's house
#CryoSleep - passenger want to be in suspended animation or not#Cabin - number of passenger's cabin
#Destination - passenger's arrival point
#Age - age of passenger
#VIP - vip passenger service
#RoomService - amount of moneys spent to room
#FoodCourt - amount of moneys spent to foodcort
#ShoppingMall - amount of moneys spent to shopping
#FoodCourt - amount of moneys spent to foodcort
#VRDeck - amount of moneys spent to upper deck
#Name - firstname and secondname of passenger
#Transported - fact was the passenger transported, target variable

data = pd.read_csv('train.csv')

#Check number of NaN in dataset
data.isnull().sum()

#Let's learn our dataset more attentively
ydata_profiling.ProfileReport(data)

#Let's replace NaN either with the average value if the variables are numeric, or with the most frequent value otherwise
data['HomePlanet'] = data['HomePlanet'].fillna(value = 'Earth')
data['CryoSleep'] = data['CryoSleep'].fillna(value = 'False')
data['Destination'] = data['Destination'].fillna(value = 'TRAPPIST-1e')
data['Age'] = data['Age'].fillna(value = data['Age'].mean())
data['VIP'] = data['VIP'].fillna(value = 'False')
data['RoomService'] = data['RoomService'].fillna(value = data['RoomService'].mean())
data['FoodCourt'] = data['FoodCourt'].fillna(value = data['FoodCourt'].mean())
data['ShoppingMall'] = data['ShoppingMall'].fillna(value = data['ShoppingMall'].mean())
data['Spa'] = data['Spa'].fillna(value = data['Spa'].mean())
data['VRDeck'] = data['VRDeck'].fillna(value = data['VRDeck'].mean())

#Transform columns to numeric values.
def transform_homePlanet(homePlanet, dictionary):
    return dictionary[homePlanet]

def transform_cryoSleep(cryoSleep):
    if cryoSleep is True:
        return 1
    else:
        return 0
    
def transform_destination(destination, dictionary):
    return dictionary[destination]

def transform_vip(vip):
    if vip is True:
        return 1
    else:
        return 0
    
def transform_transport(transport):
    if transport is True:
        return 1
    else:
        return 0

#Get dictionary of unique values in columns
def get_dict(column):
    d = {}
    for i in range(0, len(column.unique())):
        d[column.unique()[i]] = float(i)
    return d

#Dictionary for HomePlanet and Destination
dict_homePlanet = get_dict(data['HomePlanet'])
dict_destination = get_dict(data['Destination'])
data['HomePlanet'] = data['HomePlanet'].apply(lambda x: transform_homePlanet(x, dict_homePlanet))
data['CryoSleep'] = data['CryoSleep'].apply(transform_cryoSleep)
data['Destination'] = data['Destination'].apply(lambda x: transform_destination(x, dict_destination))
data['VIP'] = data['VIP'].apply(transform_vip)
data['Transported'] = data['Transported'].apply(transform_transport)

#I can delete columns PassengerId, Cabin and Name. Because they don't allow target variable
data.drop('PassengerId', axis=1, inplace=True)
data.drop('Cabin', axis=1, inplace=True)
data.drop('Name', axis=1, inplace=True)

#Let's build table of correlation
corr = data.corr()
corr.style.background_gradient(cmap='coolwarm')

#After correlation I can delete CryoSleep column
X = data.drop(['CryoSleep', 'Transported'], axis = 1)
Y = data['Transported']

#Divide datsaet in the ratio 70% for learning and 30% for test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 42)

#Create DecisionTree model. Accuracy is 0.76
tree = DecisionTreeClassifier(max_depth = 10)
tree_simple = tree.fit(X_train, Y_train)
predictions = tree_simple.predict(X_test)
print(classification_report(Y_test, predictions))

#Create RandomForestClassifier model. Accuracy is 0.76
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 42)
classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_test)
print(classification_report(Y_test, y_pred))

#Create LogisticRegression model. Accuracy is 0.74
logisticRegression = LogisticRegression(random_state = 42)
logisticRegression.fit(X_train, Y_train)
y_pred = logisticRegression.predict(X_test)
print(classification_report(Y_test, y_pred))

#Create OneVsRestClassifier model. Accuracy is 0.74
pred_proba = OneVsRestClassifier(LinearSVC(random_state=0)).fit(X_train, Y_train).predict(X_test)
print(classification_report(Y_test, pred_proba))

#Create OneVsOneClassifier model. Accuracy is 0.74
pred_proba = OneVsOneClassifier(LinearSVC(random_state=0)).fit(X_train, Y_train).predict(X_test)
print(classification_report(Y_test, pred_proba))