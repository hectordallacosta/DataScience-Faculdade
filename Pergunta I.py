import pandas as pd

# Caminho COMPLETO para o arquivo CSV, incluindo o nome do arquivo.
# Certifique-se de que "Dataset questão 1.csv" é o nome exato do seu arquivo.
file_path = r'C:\Users\hector.dallacosta\Downloads\Dataset questão 1.csv'

try:
    # 1. Carregar o dataset
    df = pd.read_csv(file_path, delimiter=';')

    # 3. Exibir informações sobre as colunas
    print("--- Informações sobre as Colunas do Dataset ---")
    df.info()
    print("\n" + "="*50 + "\n")

    # 4. Realizar e exibir estatísticas descritivas
    print("--- Estatísticas Descritivas do Dataset ---")
    print(df.describe())
    print("\n" + "="*50 + "\n")

except FileNotFoundError:
    print(f"Erro: O arquivo '{file_path}' não foi encontrado. Por favor, verifique o nome e o caminho completo do arquivo.")
except PermissionError: # Captura o erro específico de permissão
    print(f"Erro de permissão: Não foi possível acessar o arquivo ou diretório '{file_path}'.")
    print("Por favor, verifique se o arquivo não está aberto em outro programa (ex: Excel) e se você tem permissões de leitura para ele.")
except Exception as e:
    print(f"Ocorreu um erro inesperado ao processar o arquivo: {e}")