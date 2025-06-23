import pandas as pd

# Define o caminho completo para o seu arquivo CSV.
# Por favor, verifique e ajuste este caminho se o seu arquivo NÃO estiver nesta localização exata.
file_path = r'C:\Users\hector.dallacosta\Downloads\Dataset questão 1.csv' 

try:
    # Carregar o dataset com o delimitador e codificação corretos.
    df = pd.read_csv(file_path, delimiter=';', encoding='utf-8-sig')
    print(f"Dataset '{file_path}' carregado com sucesso para análise de variáveis numéricas.\n")

    # --- Análise do comportamento das variáveis numéricas (média, mediana, desvio-padrão) ---
    print("--- Comportamento das Variáveis Numéricas (Média, Mediana, Desvio-Padrão) ---")

    numerical_summary = df[['Idade', 'Valor_Compra']].describe()
    
    print("Estatísticas Descritivas para as variáveis 'Idade' e 'Valor_Compra':")
    print(numerical_summary)

    print("\n--- Análise e Interpretação ---")
    print(f"- **Idade:**")
    print(f"    - Média: {numerical_summary.loc['mean', 'Idade']:.2f} anos.")
    print(f"    - Mediana (50%): {numerical_summary.loc['50%', 'Idade']:.2f} anos.")
    print(f"    - Desvio Padrão: {numerical_summary.loc['std', 'Idade']:.2f} anos.")
    print(f"    -> A idade média é próxima da mediana, sugerindo uma distribuição relativamente simétrica.")
    print(f"    -> O desvio padrão é considerável, indicando uma ampla variação de idades entre os clientes (de {numerical_summary.loc['min', 'Idade']:.0f} a {numerical_summary.loc['max', 'Idade']:.0f} anos).")

    print(f"\n- **Valor de Compra:**")
    print(f"    - Média: R$ {numerical_summary.loc['mean', 'Valor_Compra']:.2f}.")
    print(f"    - Mediana (50%): R$ {numerical_summary.loc['50%', 'Valor_Compra']:.2f}.")
    print(f"    - Desvio Padrão: R$ {numerical_summary.loc['std', 'Valor_Compra']:.2f}.")
    print(f"    -> A mediana é ligeiramente maior que a média, o que pode indicar uma leve assimetria com mais valores menores, mas com alguns valores maiores que puxam a média.")
    print(f"    -> O desvio padrão é alto em relação à média, o que aponta para uma grande variabilidade nos valores das compras, de R$ {numerical_summary.loc['min', 'Valor_Compra']:.2f} a R$ {numerical_summary.loc['max', 'Valor_Compra']:.2f}.")
    print("\n")

except FileNotFoundError:
    print(f"Erro")