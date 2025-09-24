import pandas as pd

# Exemplo de dados
dados = {
    'produto': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'quantidade': [2, 1, 3, 5, 2, 1, 4]
}

df = pd.DataFrame(dados)

print(df)