from src.data_loader import load_csv
from src.preprocessing import clean_dataframe
from src.analysis import basic_statistics
from src.visualization import plot_histogram


def main():
    # 1. Carregar dados
    df = load_csv("data/raw/dataset.csv")

    # 2. Pré-processar
    df = clean_dataframe(df)

    # 3. Analisar
    stats = basic_statistics(df)
    print(stats)

    # 4. Visualizar
    plot_histogram(df, df.columns[0])


if __name__ == "__main__":
    main()
