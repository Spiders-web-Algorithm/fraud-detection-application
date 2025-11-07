import pandas as pd
import os

def load_transactions(file_path=None):
    """
    Load transaction data. If file_path is None, load all CSVs in data folder.
    """
    if file_path:
        data = pd.read_csv(file_path)
    else:
        # Load all CSVs in 'data/' folder
        data_files = [os.path.join("data", f) for f in os.listdir("data") if f.endswith(".csv")]
        data = pd.concat([pd.read_csv(f) for f in data_files], ignore_index=True)
    return data

def clean_data(df):
    """
    Basic cleaning: handle missing values and duplicates.
    """
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df

def feature_engineering(df):
    """
    Example feature engineering for fraud detection.
    """
    df['transaction_amount_log'] = df['transaction_amount'].apply(lambda x: 0 if x <= 0 else np.log(x))
    df['hour'] = pd.to_datetime(df['transaction_date']).dt.hour
    df['day_of_week'] = pd.to_datetime(df['transaction_date']).dt.dayofweek
    return df
