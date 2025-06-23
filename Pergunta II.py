import pandas as pd

# Define o caminho completo para o seu arquivo CSV.
# Por favor, verifique e ajuste este caminho se o seu arquivo NÃO estiver nesta localização exata.
file_path = r'C:\Users\hector.dallacosta\Downloads\Dataset questão 1.csv' 

try:
    # Carregar o dataset com o delimitador e codificação corretos.
    df = pd.read_csv(file_path, delimiter=';', encoding='utf-8-sig')
    print(f"Dataset '{file_path}' carregado com sucesso para verificação de dados ausentes/inconsistentes.\n")

    # --- ii. Há dados ausentes ou inconsistentes? ---
    print("--- Verificação de Dados Ausentes e Inconsistentes ---")

    # 1. Contagem de valores ausentes (NaN/None) por coluna
    missing_data = df.isnull().sum()
    print("1. Contagem de valores ausentes por coluna:")
    print(missing_data)

    # 2. Verificação de inconsistências em colunas categóricas (valores únicos)
    # Isso ajuda a identificar erros de digitação ou variações inesperadas.
    print("\n2. Valores únicos para colunas categóricas (para identificar inconsistências):")
    print("   - Localização:", df['Localização'].unique())
    print("   - Canal_Aquisição:", df['Canal_Aquisição'].unique())
    print("   - Produto:", df['Produto'].unique())


except FileNotFoundError:
    print(f"Erro: O arquivo '{file_path}' não foi encontrado. Por favor, verifique o nome e o caminho completo do arquivo.")