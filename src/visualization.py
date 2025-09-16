import matplotlib.pyplot as plt

def plot_histogram(df, column: str):
    """Plota histograma de uma coluna numérica."""
    plt.figure(figsize=(8,5))
    df[column].hist(bins=30)
    plt.title(f"Distribuição de {column}")
    plt.show()
