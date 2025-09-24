import matplotlib.pyplot as plt
import streamlit as st

def plot_histogram(df, column: str):
    """Plota histograma de uma coluna numérica."""
    plt.figure(figsize=(8,5))
    df[column].hist(bins=30)
    plt.title(f"Distribuição de {column}")
    plt.show()

def streamlit_start(df, manufacturers):
    st.title("Analise de produtos vendidos por fornecedor")
    st.text_area(placeholder=manufacturers, label="Fornecedores Analisados")
    st.dataframe(df)
    st.bar_chart(df, x="Descricao do Produto", y="Qtde",)

