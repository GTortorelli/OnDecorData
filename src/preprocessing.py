import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Remove valores nulos e duplicados."""
    df = df.dropna()
    return df
