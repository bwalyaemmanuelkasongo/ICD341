import pandas as pd

def load_data(filepath):
    """Load the maize production data."""
    return pd.read_csv(filepath)

def calculate_mean(df):
    """Calculate the mean production."""
    return df['Production'].mean()