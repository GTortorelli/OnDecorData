import pandas as pd

def basic_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna estatísticas descritivas básicas."""
    # return df.describe()
    return 0

def most_sold(df: pd.DataFrame):
    most_sold = df.groupby('Descricao do Produto')['Qtde'].idxmax()
    return most_sold

def sorted_df(df: pd.DataFrame):
    # print(df.sort_values(by='Qtde', ascending=False))
    return df.sort_values(by='Qtde', ascending=False)

def get_manufacturers_list(df: pd.DataFrame):
    unique_manufacturers = df['Fabricante'].unique().astype(str)
    stripped_manufacturers = [x.strip() for x in unique_manufacturers]
    
    return stripped_manufacturers