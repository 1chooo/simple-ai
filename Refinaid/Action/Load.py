from os.path import join
from os.path import dirname
from os.path import abspath
import pandas as pd
import time 

def get_dataframe(dataset_name: str) -> pd.DataFrame:
    try:
        dataset_mapping = {
            'Titanic'     : 'titanic.csv',
            'House Prices': 'house_prices.csv',
            'Diabetes'    : 'diabetes.csv'
        }

        file_path = join(
            dirname(abspath(__file__)),
            '..', 
            '..', 
            'data', 
            dataset_name.lower().replace(' ', '_'),
            dataset_mapping.get(dataset_name, '')
        )

        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(e)
        return None


def test_load_dataframe(dataset_name: str):
    start_time = time.time()
    df = get_dataframe(dataset_name)
    print('Time used: ', time.time() - start_time)
    print(df.head())
    print('Time used: ', time.time() - start_time)
    return None

# test_load_dataframe('Titanic')
