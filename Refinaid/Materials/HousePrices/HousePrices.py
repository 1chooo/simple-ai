# %% [markdown]
# # Final Exam - New York City Taxi Fare Prediction
# 
# Course: AP4063
# 
# Student Number: 109601003
# 
# Name: 林群賀
# 
# #### Baseline: 4.03742

# %%
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# import os
# import matplotlib.pyplot as plt
# import seaborn as sns

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# %% [markdown]
# ## Import the package

# %%
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from zipfile import ZipFile

# %% [markdown]
# ## Import the data sets.

# %%
data_path = os.getcwd()
train_data_path = data_path + '/kaggle/input/taxi_fare_train.csv'
test_data_path = data_path + '/kaggle/input/taxi_fare_test.csv'

df_train = pd.read_csv('/kaggle/input/new-york-city-taxi-fare-prediction/train.csv', nrows=500_000)
df_test = pd.read_csv('/kaggle/input/new-york-city-taxi-fare-prediction/test.csv')

# %%
df_train.info()

# %%
df_train.head()

# %%
df_train.describe()

# %% [markdown]
# #### I found that there were a lot of unreasonable data, so I corrected them by replacing them with the average. However, even with these changes, the score I obtained was 8.73076, which is not higher than the baseline.

# %%
# df_train[df_train['pickup_longitude'] < -73.992047] = -73.981785
# df_train[df_train['pickup_latitude'] < 40.734917] = 40.752670
# df_train[df_train['pickup_longitude'] > -73.967117] =  -73.981785
# df_train[df_train['pickup_latitude'] < 40.767076] = 40.752670

# df_train[df_train['dropoff_longitude'] < -73.991382] = -73.980126
# df_train[df_train['dropoff_latitude'] < 40.734057] = 40.753152
# df_train[df_train['dropoff_longitude'] > -73.963572] =  -73.980126
# df_train[df_train['dropoff_latitude'] < 40.768135] = 40.753152

# df_train.describe()

# %%
train_Y = np.array(df_train['fare_amount'])
ids = df_test['key']

df_train = df_train.drop(['key', 'fare_amount'] , axis=1)
df_test = df_test.drop(['key'] , axis=1)
df = pd.concat([df_train,df_test])

df.head()

# %%
df_train['diff_lat'] = (df_train['dropoff_latitude'] - df_train['pickup_latitude']).abs()
df_train['diff_long'] = (df_train['dropoff_longitude'] - df_train['pickup_longitude'] ).abs()

df_test['diff_lat'] = (df_test['dropoff_latitude'] - df_test['pickup_latitude']).abs()
df_test['diff_long'] = (df_test['dropoff_longitude'] - df_test['pickup_longitude'] ).abs()

# %%
df_train.head()

# %% [markdown]
# #### With this plot, we can observe that the passengers almost take the taxi in the same place.

# %%
plot = df_train.iloc[:2000].plot.scatter('diff_long', 'diff_lat')

# %% [markdown]
# #### By using the mean of the latitude and longitude, I was able to achieve a score of 9.40441. However, this score is still not higher than the baseline.

# %%
# df['distance_2D'] = (
#     (df['dropoff_longitude'].mean() - df['pickup_longitude'].mean()) ** 2 + \
#     (df['dropoff_latitude'].mean() - df['pickup_latitude'].mean()) ** 2) ** 0.5

# %%
df['distance_2D'] = (
    (df['dropoff_longitude'] - df['pickup_longitude']) ** 2 + \
    (df['dropoff_latitude'] - df['pickup_latitude']) ** 2) ** 0.5


df = df.drop(['pickup_longitude', 
              'pickup_latitude', 
              'dropoff_longitude', 
              'dropoff_latitude', 
              'pickup_datetime'
              ], axis=1)
              
df.head()

# %%
df['passenger_count'] = df['passenger_count'].fillna(-1)
df['distance_2D'] = df['distance_2D'].fillna(-1)

# %% [markdown]
# ## Prediction
# 
# #### With the Gradient Boosting Machine Model

# %%
from sklearn import datasets, metrics
from sklearn.ensemble import GradientBoostingRegressor

# %%
train_num = train_Y.shape[0]
train_X = df[:train_num]
test_X = df[train_num:]

reg = GradientBoostingRegressor()
reg.fit(train_X, train_Y)
pred = reg.predict(test_X)

# %% [markdown]
# ## Output the Results

# %%
pred = np.array(pred)
sub = pd.DataFrame({'key': ids, 'fare_amount': pred})
sub.to_csv('/kaggle/working/submission.csv', index=False) 

# %%
# data_path = os.getcwd()
# data_path += "/data/my_result/"
# pred = np.array(pred)
# sub = pd.DataFrame({'key': ids, 'fare_amount': pred})
# sub.to_csv(data_path + 'taxi_1111_finalexam.csv', index=False) 

# %% [markdown]
# ## My Result
# 
# #### The screenshot
# 
# ![the result](./data/my_result/taxi_1111_finalexam.png)

# %% [markdown]
# ## What I have tried?
# 
# 1. 
#    I attempted to process the data because some of the latitude and longitude values were not reasonable, particularly the maximum and minimum values. However, after replacing them, the results were not as expected. 
# 
#    Therefore, based on my previous experience with the Titanic random forest, I was afraid that errors would propagate to an uncontrollable extent. 
#    
#    As a result, I chose to adopt the baseline approach.

# %% [markdown]
# ## Reference
# 
# [New York City Taxi Fare Prediction](https://medium.com/analytics-vidhya/new-york-city-taxi-fare-prediction-1ba96223ba7e)
# 
# [NYC Taxi Fare Prediction](https://towardsdatascience.com/nyc-taxi-fare-prediction-605159aa9c24)
# 
# [New-York-City-Taxi-Fare-Prediction-Machine-Learning](https://github.com/nikoshet/New-York-City-Taxi-Fare-Prediction-Machine-Learning/blob/master/Machine_Learning_Project.ipynb)
# 
# [NYC Taxi Fare Prediction with Gradient Boosting Algorithm](https://towardsdatascience.com/nyc-taxi-fare-prediction-with-gradient-boosting-algorithm-9ff7a1eded1e)

