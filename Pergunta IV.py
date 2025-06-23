import pandas as pd

# Define o caminho completo para o seu arquivo CSV.
# Por favor, verifique e ajuste este caminho se o seu arquivo NÃO estiver nesta localização exata.
file_path = r'C:\Users\hector.dallacosta\Downloads\Dataset questão 1.csv' 

try:
    # Carregar o dataset com o delimitador e codificação corretos.
    df = pd.read_csv(file_path, delimiter=';', encoding='utf-8-sig')
    print(f"Dataset '{file_path}' carregado com sucesso para análise de produtos por localidade.\n")

    # --- iv. Clientes de determinada localidade compram mais um certo produto? ---
    print("--- Análise de Produtos por Localidade ---")

    # Agrupar os dados por 'Localização' e 'Produto' e contar o número de ocorrências (compras).
    # O .unstack(fill_value=0) transforma a série agrupada em uma tabela pivô,
    # onde as localidades são índices e os produtos são colunas, facilitando a visualização.
    product_sales_by_location = df.groupby(['Localização', 'Produto']).size().unstack(fill_value=0)
    
    print("Número de compras de cada produto por Localização:")
    print(product_sales_by_location)

    # Para identificar se um certo produto é mais comprado em uma determinada localidade,
    # podemos encontrar a combinação (Localização, Produto) com o maior número de compras.
    if not product_sales_by_location.empty:
        # stack() transforma a tabela em uma série novamente, facilitando encontrar o máximo.
        most_bought_combination = product_sales_by_location.stack().idxmax()
        max_purchases_count = product_sales_by_location.stack().max()
        print(f"\nSim, há preferências. A combinação (Localização, Produto) com o maior número de compras é: {most_bought_combination}, com {max_purchases_count} compras.")
        print("\nPara uma análise mais detalhada, você pode observar a tabela acima e identificar o produto com maior número de vendas para cada localidade individualmente.")
    else:
        print("\nNão foi possível determinar a preferência por localidade e produto, pois a tabela de vendas está vazia.")
    print("-" * 50 + "\n")

except FileNotFoundError:
    print(f"Erro")