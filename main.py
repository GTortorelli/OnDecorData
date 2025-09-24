from src.data_loader import load_csv
from src.preprocessing import clean_dataframe
from src.analysis import basic_statistics, most_sold, sorted_df, get_manufacturers_list
from src.visualization import streamlit_start


def main():
    # 1. Carregar dados
    df = load_csv("data/raw/VendaFabricante.Csv")

    # 2. Pré-processar
    # df = clean_dataframe(df)

    # 3. Analisar
    most_sold_item = most_sold(df)
    sorted_dataframe = sorted_df(df)
    print(sorted_dataframe)
    manufacturers = get_manufacturers_list(df)
    
    # 4. Visualizar
    # plot_histogram(df, df.columns[0])
    streamlit_start(sorted_dataframe, manufacturers)


if __name__ == "__main__":
    main()

