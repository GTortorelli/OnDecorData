import pandas as pd

def load_csv(filepath: str) -> pd.DataFrame:
    """Carrega um dataset CSV em um DataFrame pandas."""
    return pd.read_csv(filepath, sep=";")
