import pandas as pd

# Define o caminho completo para o seu arquivo CSV.
# Por favor, verifique e ajuste este caminho se o seu arquivo NÃO estiver nesta localização exata.
file_path = r'C:\Users\hector.dallacosta\Downloads\Dataset questão 1.csv' 

try:
    # Carregar o dataset com o delimitador e codificação corretos.
    df = pd.read_csv(file_path, delimiter=';', encoding='utf-8-sig')
    print(f"Dataset '{file_path}' carregado com sucesso para análise de receita por canal de aquisição.\n")

    # --- Qual canal de aquisição traz mais receita? ---
    print("--- Análise de Receita por Canal de Aquisição ---")

    # Agrupar os dados por 'Canal_Aquisição' e somar o 'Valor_Compra' para cada grupo.
    # O .sort_values(ascending=False) ordena os resultados do maior para o menor.
    revenue_by_acquisition_channel = df.groupby('Canal_Aquisição')['Valor_Compra'].sum().sort_values(ascending=False)
    
    print("Receita total por Canal de Aquisição:")
    print(revenue_by_acquisition_channel)

    # Identificar o canal que gerou a maior receita.
    if not revenue_by_acquisition_channel.empty:
        highest_revenue_channel = revenue_by_acquisition_channel.index[0]
        highest_revenue_amount = revenue_by_acquisition_channel.iloc[0]
        print(f"\nO canal de aquisição que traz mais receita é: '{highest_revenue_channel}' com um total de R$ {highest_revenue_amount:.2f}.")
    else:
        print("\nNão foi possível determinar o canal de aquisição com maior receita, pois a tabela de receitas está vazia.")
    print("-" * 50 + "\n")

except FileNotFoundError:
    print(f"Erro")