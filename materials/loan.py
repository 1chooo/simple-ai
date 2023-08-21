# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

dataFrame = pd.read_csv("./loan_prediction_training_data.csv")
dataFrame.head()
dataFrame.describe()
dataFrame.describe().T
dataFrame.info()

dataFrame["Credit_History"].value_counts()
dataFrame["Self_Employed"].value_counts()
dataFrame["Property_Area"].value_counts()
dataFrame["Education"].value_counts()

dataFrame["ApplicantIncome"].hist(bins = 200)
dataFrame.boxplot(column = "ApplicantIncome", by = "Education")

dataFrame["LoanAmount"].hist(bins = 200)
dataFrame.boxplot(column = "LoanAmount", by = "Self_Employed")

temp1 = dataFrame["Credit_History"].value_counts(ascending = True)
temp2 = dataFrame.pivot_table(values = "Loan_Status", index = ["Credit_History"], aggfunc = lambda x: x.map({'Y': 1, 'N': 0}).mean())


""" We can try other data type to observe. """
temp1.plot(kind = "bar")
temp2.plot(kind = "bar", yticks = [0, 0.5, 1])
figure = plt.figure(figsize = (8, 4))

temp5 = pd.crosstab(dataFrame["Credit_History"], dataFrame["Loan_Status"])
temp5.plot(kind = "bar", stacked = True, grid = True)

""" We can also cross more than one datatype. """
temp5 = pd.crosstab([dataFrame["Credit_History"], dataFrame["Gender"]], dataFrame["Loan_Status"])
temp5.plot(kind = "bar", stacked = True, grid = True)


""" Solve the missing value. """

# The method we choose to fill the missing value 
# is through showing the most frequently data.

dataFrame.isnull().sum().sort_values(ascending = False)
dataFrame.apply(lambda x:sum(x.isnull()),axis=0).sort_values(ascending=False)


dataFrame["Self_Employed"].value_counts()
print(500 / (500 + 82))
dataFrame["Self_Employed"].fillna("No", inplace = True)

""" The other way to fill the missing values. """
# Be careful to check the index we use is not lacking.

table = dataFrame.pivot_table(values = "LoanAmount", index = "Self_Employed", columns = "Education", aggfunc = np.median)
# Manually
table.loc["Yes", "Graduate"]
table.loc["No", "Not Graduate"]

# Auto

def fage(x):
    return table.loc[x["Self_Employed"], x["Education"]]

dataFrame["LoanAmount"].fillna(dataFrame.apply(fage, axis = 1), inplace = True)


dataFrame["LoanAmount_log"] = np.log(dataFrame["LoanAmount"])
dataFrame["LoanAmount_log"].hist(bins = 200)


dataFrame["TotalIncome"] = dataFrame["ApplicantIncome"] + dataFrame["CoapplicantIncome"]
dataFrame["TotalIncome_log"] = np.log(dataFrame["TotalIncome"])
dataFrame["TotalIncome_log"].hist(bins = 200)


dataFrame["Gender"].value_counts()
dataFrame["Gender"].mode()[0]

# we use the most frequency value to fill the missing value.
 
dataFrame["Gender"].fillna(dataFrame["Gender"].mode()[0], inplace = True)
dataFrame["Married"].fillna(dataFrame["Married"].mode()[0], inplace = True)
dataFrame["Dependents"].fillna(dataFrame["Dependents"].mode()[0], inplace = True)
dataFrame["Loan_Amount_Term"].fillna(dataFrame["Loan_Amount_Term"].mode()[0], inplace = True)
dataFrame["Credit_History"].fillna(dataFrame["Credit_History"].mode()[0], inplace = True)

dataFrame.info()

# If Dtype equals object we need to diverse into numerical number.

""" Convert types from object to numerical number. """

from sklearn.preprocessing import LabelEncoder

# Then we pick up something that is related to diverse.

var_mod = ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Property_Area", "Loan_Status"]

# Before we continue we can check the most frequency types of value.

dataFrame["Gender"].value_counts()
dataFrame["Married"].value_counts()
dataFrame["Dependents"].value_counts()
dataFrame["Education"].value_counts()
dataFrame["Self_Employed"].value_counts()
dataFrame["Property_Area"].value_counts()
dataFrame["Loan_Status"].value_counts()

labelEncoder = LabelEncoder()

for i in var_mod:
    dataFrame[i] = labelEncoder.fit_transform(dataFrame[i])


""" Send the model to let machine learn. """

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score

def LoanModel(model, data, predictors, outcome, testSize, randomStateNumber) :
    x = data[predictors]
    y = data[outcome]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = testSize, random_state = randomStateNumber)
    model.fit(x_train, y_train)     # this line we have done the module
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    print(f"Accuracy:{accuracy}")
    print(f"Recall:{recall}")
    print(f"Precision:{precision}")



""" A series of little experiment to chwck how accurate of the module. """

# The first experiment

outcome_var = "Loan_Status"
model = LogisticRegression()
predictor_var = ["Credit_History"]
LoanModel(model, dataFrame, predictor_var, outcome_var, 0.3, 6)

# The second experiment, we want to check 
# whether the different module wil make the different outcome
# it's because that our data is too small.

outcome_var = "Loan_Status"
model2 = DecisionTreeClassifier()
predictor_var = ["Credit_History"]
LoanModel(model2, dataFrame, predictor_var, outcome_var, 0.3, 6)

# The third experiment, we add more variable to check

outcome_var = "Loan_Status"
model3 = LogisticRegression()
predictor_var = ["Credit_History", "Gender", "Married", "Education"]
LoanModel(model3, dataFrame, predictor_var, outcome_var, 0.3, 6)

# The forth experiment, we also use the different module to 
# check the outcome.

outcome_var = "Loan_Status"
model3 = RandomForestClassifier(n_estimators=10)     # we can change more trees in this module
predictor_var = ["Credit_History", "Gender", "Married", "Education"]
LoanModel(model3, dataFrame, predictor_var, outcome_var, 0.3, 6)

# The fifth experiment, we add more variable; however we didn't find more accurate

outcome_var = 'Loan_Status'
model4 = RandomForestClassifier(n_estimators=10)
predictor_var = ['Credit_History','Gender','Married','Education','Dependents','Self_Employed', 'Property_Area','LoanAmount_log','TotalIncome_log']
LoanModel(model4, dataFrame, predictor_var, outcome_var, 0.3, 6)

# The sixth experiment, we conbine the first and the fifth experiment

outcome_var = 'Loan_Status'
model5 = LogisticRegression()
predictor_var = ['Credit_History','Gender','Married','Education','Dependents','Self_Employed', 'Property_Area','LoanAmount_log','TotalIncome_log']
LoanModel(model5, dataFrame, predictor_var, outcome_var, 0.3, 6)

""" 
We will pick the last version of wxperiment to 
suit the user interface, then we will do it the next. 
"""


# We have a lot of data, but we only pick up one of them.
# This allow lots of data to be tested.
model.predict([[1, 1, 1, 1, 1, 1, 1, np.log(150), np.log(5000)]])

""" Export the module. """
import joblib
joblib.dump(model, "LoanOrNot-LR-20220502.pkl", compress=3)