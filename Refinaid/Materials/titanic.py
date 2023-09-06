# %% [markdown]
# # Final Exam - Titanic
# 
# Course: AP4063
# 
# Student Number: 109601003
# 
# Name: 林群賀
# 
# #### Baseline: 0.78708

# %% [markdown]
# ## Import the package

# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ## Import the data sets.

# %%
data_path = os.getcwd()
train_data_path = data_path + '/data/titanic_train.csv'
test_data_path = data_path + '/data/titanic_test.csv'

df_train = pd.read_csv(train_data_path)
df_test = pd.read_csv(test_data_path)

# %%
df_train.info()

# %% [markdown]
# ## Plot charts between multiple variables

# %% [markdown]
# ### age

# %%
fig, ax=plt.subplots(1,figsize=(8,6))
sns.boxplot(x='Survived',y='Age', data=df_train)
ax.set_ylim(0,100)
plt.title("Survived vs Age")
plt.show()

# %% [markdown]
# ### Sex

# %%
fig, ax=plt.subplots(1,figsize=(8,6))
sns.countplot(x='Survived' ,hue='Sex', data=df_train)
ax.set_ylim(0,500)
plt.title("Survived vs Sex")
plt.show()

# %% [markdown]
# ### Pclass
# 

# %%
fig, ax=plt.subplots(1,figsize=(8,6))
sns.countplot(x='Survived' ,hue='Pclass', data=df_train)
ax.set_ylim(0,400)
plt.title("Survived vs Pclass")
plt.show()

# %% [markdown]
# ### Embarked

# %%
fig, ax=plt.subplots(1,figsize=(8,6))
sns.countplot(x='Survived' ,hue='Embarked', data=df_train)
ax.set_ylim(0,500)
plt.title("Survived vs Embarked")
plt.show()

# %%
train_Y = df_train['Survived']
ids = df_test['PassengerId']
df_train = df_train.drop(['PassengerId', 'Survived', 'Name', 'Ticket','Cabin'] , axis=1)
df_test = df_test.drop(['PassengerId', 'Name', 'Ticket','Cabin'] , axis=1)

combine = [df_train, df_test]

for df in combine:
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# %%
df_test.head()

# %%
df_train = df_train.drop(['SibSp', 'Parch'] , axis=1)
df_test = df_test.drop(['SibSp', 'Parch',] , axis=1)

# %%
df = pd.concat([df_train,df_test])

df.head()

# %%
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

MMEncoder = MinMaxScaler()
LEncoder = LabelEncoder()

for c in df.columns:
    if df[c].dtype == 'object':
        df[c] = df[c].fillna('None')
        df[c] = LEncoder.fit_transform(df[c]) 
    else:
        df[c] = df[c].fillna(-1)
    df[c] = MMEncoder.fit_transform(df[c].values.reshape(-1, 1))

df.head()

# %% [markdown]
# ## Prediction
# 
# #### With the Gradient Boosting Machine Model

# %%
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier


train_num = train_Y.shape[0]
train_X = df[:train_num]
test_X = df[train_num:]

clf = GradientBoostingClassifier()
clf.fit(train_X, train_Y)
pred = clf.predict(test_X)
pred = np.array(pred)

# %% [markdown]
# ## Output the Results

# %%
sub = pd.DataFrame({'PassengerId': ids, 'Survived': pred})
sub.to_csv(data_path + '/data/my_result/Titanic_1111_finalexam.csv', index=False) 

# %% [markdown]
# ## My Result
# 
# #### The screenshot
# 
# ![the result](./data/my_result/Titanic_1111_finalexam.png)

# %% [markdown]
# ## What I have tried?
# 
# 1. 
#    In the progress, I have tried using the "Random Forest" model, but it was less accurate than the baseline. 
#    
#    To improve the accuracy, I searched for various methods and found the article "Titanic Competition: Journey to 100% Accuracy". 
#    
#    In this article, the author pre-processed many variables, especially "Name," "Sex," "SibSp," "Parch," and "Age." He/She combined the names into new titles and considered the correlation between age and sex. This led to increased accuracy in the Random Forest model. 
#    
#    Overall, I learned that imbalanced data can negatively impact the accuracy of "Random Forest" and can lead to overfitting due to the presence of noise. To improve the accuracy of the model, I must be more careful in observing data types and ensure the data is balanced.
# 
# 2. 
#    Finally, the only selection was to combine 'SibSp', 'Parch' and still implemented through gradient boosting model. At first, when I saw this method, I thought it was quite cool. 
#    
#    After all, having children and having relatives are two relationships with a lot of possibilities, and it is possible that there are overlapping possibilities. So, combining them together is a choice that may be worth trying to deal with the data.

# %% [markdown]
# ## Reference
# 
# [Titanic Competition [Journey to 100% Accuracy]](https://www.kaggle.com/code/amerwafiy/titanic-competition-journey-to-100-accuracy)
# 
# [[機器學習專案] Kaggle競賽-鐵達尼號生存預測(Top 3%)](https://yulongtsai.medium.com/https-medium-com-yulongtsai-titanic-top3-8e64741cc11f)
# 
# [[資料分析&機器學習] 第4.1講 : Kaggle競賽-鐵達尼號生存預測(前16%排名)](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC4-1%E8%AC%9B-kaggle%E7%AB%B6%E8%B3%BD-%E9%90%B5%E9%81%94%E5%B0%BC%E8%99%9F%E7%94%9F%E5%AD%98%E9%A0%90%E6%B8%AC-%E5%89%8D16-%E6%8E%92%E5%90%8D-a8842fea7077)

