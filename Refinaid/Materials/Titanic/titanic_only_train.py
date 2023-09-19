# -*- coding: utf-8 -*-

"""
This code is from the machine learning course
and the main goal of this code is to predict
the trend of Titanic surviving situation.
"""

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

df = pd.read_csv("./train_data_titanic.csv")
df.head()
df.info()

""" Remove the unused column data. """

df.drop(["Name", "Ticket"], axis = 1, inplace = True)
df.head()

""" Observe the relation of "Survived" and others. """

sns.pairplot(df[["Survived", "Fare"]], dropna = True)
# sns.pairplot(df[["Survived", "Age"]], dropna = True)
# sns.pairplot(df[["Survived", "Sex"]], dropna = True)    # only male and female
# sns.pairplot(df[["Survived", "Pclass"]], dropna = True)
sns.pairplot(df[["Survived", "Fare"]], dropna = True)
# sns.pairplot(df[["Survived", "SibSp"]], dropna = True)
# sns.pairplot(df[["Survived", "Parch"]], dropna = True)
# sns.pairplot(df[["Survived", "Embarked"]], dropna = True)

""" 
Here we can observe the data, 
and we can obverse that the people 
who are older and pay more on tickets
the surviving percentage gets higher.
"""

df.groupby("Survived").mean()

""" Show the correspond value. """

df["SibSp"].value_counts()
df['Parch'].value_counts()
df['Sex'].value_counts()

""" Do this then we can check the missing data. """

df.isnull().sum()
len(df)
len(df) / 2
df.isnull().sum() > len(df) / 2

""" Check "Cabin" and "Age" because they have too many losing data. """

df.drop("Cabin", axis = 1, inplace = True)
df.head()
df["Age"].isnull().value_counts()
df.groupby("Sex")["Age"].median().plot(kind = "bar")

""" Use the median of male and female age to fill the losing place. """

df["Age"] = df.groupby("Sex")["Age"].apply(lambda x: x.fillna(x.median()))
df.groupby("Sex")["Age"].median()

""" Keep check whether the data still lose. """

df.isnull().sum()

df["Embarked"].value_counts()
df["Embarked"].value_counts().idxmax()
df["Embarked"].fillna(df["Embarked"].value_counts().idxmax(),inplace = True) 
df["Embarked"].value_counts()


""" Now we finish the losing value. """

df.isnull().sum()

df = pd.get_dummies(data = df, columns = ["Sex", "Embarked"])
df.head()

df.drop("Sex_female", axis = 1, inplace = True)

df["Fare"].max()
df["Fare"].min()
df["Fare"].median()

df.corr()

x = df.drop(["Survived", "Pclass"], axis = 1)
y = df["Survived"]

from sklearn.model_selection import train_test_split

""" Split to training and testing data. """
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 99)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(x_train, y_train)
predictions = lr.predict(x_test)


from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score 
accuracy_score(y_test, predictions)
recall_score(y_test, predictions)
precision_score(y_test, predictions)
pd.DataFrame(confusion_matrix(y_test, predictions), columns=['Predict not Survived', 'Predict Survived'], index=['True not Survived', 'True Survived'])

import joblib 
joblib.dump(lr,'Titanic-LR-20220409.pkl',compress = 3)

df.head()

df['Pclass'].value_counts()
df.groupby("Pclass").mean()