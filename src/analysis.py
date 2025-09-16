import pandas as pd

def basic_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna estatísticas descritivas básicas."""
    return df.describe()
