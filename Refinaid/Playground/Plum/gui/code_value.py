# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/27
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.6
'''

data_preprocessing = """
def data_preprocessing(df: pd.DataFrame):
    columns_to_drop = [
        'ObsTime'       , 'SeaPres'       , 'StnPresMaxTime', 
        'StnPresMinTime', 'T Max Time'    , 'T Min Time'    , 
        'Td dew point'  , 'RHMinTime'     , 'WGustTime'     , 
        'PrecpHour'     , 'PrecpMax10'    , 'PrecpMax10Time', 
        'PrecpMax60'    , 'PrecpMax60Time', 'SunShine'      , 
        'SunShineRate'  , 'GloblRad'      , 'VisbMean'      , 
        'EvapA'         , 'UVI Max'       , 'UVI Max Time'  ,  
        'Cloud Amount'
    ]
    df = drop_irrelevant_col(df, columns_to_drop)

    df = replace_missing_value(df)
    df = convert_float64(df)
    df = binarize_column(df, 12)

    observed_averages = calculate_observed_averages(df)
    columns_to_fill = [0, 1, 2, 3, 4, 5, 8, 10]
    average_values = observed_averages[:8]
    df = fill_missing_values_with_averages(df, columns_to_fill, average_values)
    
    columns_to_fill = [
        (6, 'RH'), 
        (7, 'RHMin'), 
        (9, 'WD'), 
        (11, 'WDGust')
    ]
    df = fill_missing_values_with_most_common(df, columns_to_fill)

    return df
"""

drop_irrelevant_col = """
def drop_irrelevant_col(df: pd.DataFrame, columns_to_drop) -> pd.DataFrame:
    df.drop(columns_to_drop, axis=1, inplace=True)
    return df
"""

replace_missing_value = """
def replace_missing_value(df:pd.DataFrame) -> pd.DataFrame:
    # Replace missing values
    df.replace(['...', '/'], '-999', inplace=True)
    df.replace('-999', 0.0, inplace=True)

    return df
"""

convert_float64 = """
def convert_float64(df:pd.DataFrame) -> pd.DataFrame:
    # Convert DataFrame to float64
    df = pd.DataFrame(df, dtype = np.float64)

    return df
"""

binarize_column = """
def binarize_column(df:pd.DataFrame, column_index:int) -> pd.DataFrame:
    for k in range(len(df)):
        if df.iloc[k, column_index] > 0.0:
            df.iloc[k, column_index] = 1
        else:
            df.iloc[k, column_index] = 0

    return df
"""

calculate_observed_averages = """
def calculate_observed_averages(df:pd.DataFrame) -> list:
    observed_columns_indices = [0, 1, 2, 3, 4, 5, 8, 10]
    observation_counts = [0] * len(observed_columns_indices)
    observation_totals = [0] * len(observed_columns_indices)

    for row_index in range(len(df)):
        for col_index, obs_col_idx in enumerate(observed_columns_indices):
            if df.iloc[row_index, obs_col_idx] != -999.0:
                value = float(df.iloc[row_index, obs_col_idx])
                observation_counts[col_index] += 1
                observation_totals[col_index] += value

    observed_averages = [
        round(total / count, 1) if count > 0 else 0 for total, count in zip(observation_totals, observation_counts)
    ]

    return observed_averages
"""

fill_missing_values_with_averages = """
def fill_missing_values_with_averages(
        df:pd.DataFrame, columns_to_fill:list, average_values:list) -> pd.DataFrame:
    for c in range(len(df)):
        for col_idx, avg_value in zip(columns_to_fill, average_values):
            if df.iloc[c, col_idx] == -999.0:
                df.iloc[c, col_idx] = avg_value

    return df
"""

fill_missing_values_with_most_common = """
def fill_missing_values_with_most_common(df:pd.DataFrame, columns_to_fill:list) -> pd.DataFrame:
    for col_idx, col_name in columns_to_fill:
        for i in range(len(df)):
            if df.iloc[i, col_idx] == -999.0:
                df.iloc[i, col_idx] = df[col_name].value_counts().idxmax()

    return df
"""

train_logistic_regression = """
def train_logistic_regression(df):
    X = df.drop(['Precp'], axis=1)
    y = df['Precp']
    X = X.values # conversion of X into array

    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y, 
        test_size=0.3, 
        random_state=67,
    )
    
    lr = LogisticRegression(max_iter=200)
    lr.fit(X_train, y_train)

    predictions = lr.predict(X_test)

    return lr, X_test, y_test, predictions
"""

evaluate_model = """
def evaluate_model(y_test, predictions):
    accuracy = accuracy_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    confusion = pd.DataFrame(
        confusion_matrix(y_test, predictions), 
        columns=['Predict not rain', 'Predict rain'], 
        index=['True not rain', 'True rain']
    )

    return accuracy, recall, precision, confusion
"""
