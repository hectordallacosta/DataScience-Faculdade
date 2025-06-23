import pandas as pd
from datetime import datetime

# Define o caminho completo para o seu arquivo CSV.
# AJUSTE ESTE CAMINHO se necessário.
file_path = r'C:\Users\hector.dallacosta\Downloads\Dataset questão 1.csv' 

try:
    # Carregar o dataset com o delimitador e codificação corretos.
    df = pd.read_csv(file_path, delimiter=';', encoding='utf-8-sig')
    print(f"Dataset '{file_path}' carregado com sucesso para verificação de valores fora do esperado.\n")

    print("--- Verificação de Valores Fora do Esperado (Outliers e Inconsistências Lógicas) ---\n")

    # --- Análise de 'Idade' ---
    print("Análise da Coluna: Idade")
    print(f"Mínimo: {df['Idade'].min()}, Máximo: {df['Idade'].max()}")

    Q1_idade = df['Idade'].quantile(0.25)
    Q3_idade = df['Idade'].quantile(0.75)
    IQR_idade = Q3_idade - Q1_idade
    lower_bound_idade = Q1_idade - 1.5 * IQR_idade
    upper_bound_idade = Q3_idade + 1.5 * IQR_idade

    outliers_idade = df[(df['Idade'] < lower_bound_idade) | (df['Idade'] > upper_bound_idade)]
    if not outliers_idade.empty:
        print(f"**ALERTA**: Outliers detectados na coluna 'Idade' (fora do intervalo [{lower_bound_idade:.2f}, {upper_bound_idade:.2f}]):")
        print(outliers_idade[['ID_Cliente', 'Idade']])
    else:
        print("Nenhum outlier significativo detectado na coluna 'Idade' pelo método IQR.")
    
    # Verificação de valores logicamente impossíveis (idade negativa ou zero)
    if df['Idade'].min() <= 0:
        print(f"**ALERTA**: Idade mínima ({df['Idade'].min()}) é zero ou negativa, o que é um valor inesperado.")
    print("-" * 50)

    # --- Análise de 'Valor_Compra' ---
    print("\nAnálise da Coluna: Valor_Compra")
    print(f"Mínimo: {df['Valor_Compra'].min():.2f}, Máximo: {df['Valor_Compra'].max():.2f}")

    Q1_valor = df['Valor_Compra'].quantile(0.25)
    Q3_valor = df['Valor_Compra'].quantile(0.75)
    IQR_valor = Q3_valor - Q1_valor
    lower_bound_valor = Q1_valor - 1.5 * IQR_valor
    upper_bound_valor = Q3_valor + 1.5 * IQR_valor

    outliers_valor = df[(df['Valor_Compra'] < lower_bound_valor) | (df['Valor_Compra'] > upper_bound_valor)]
    if not outliers_valor.empty:
        print(f"**ALERTA**: Outliers detectados na coluna 'Valor_Compra' (fora do intervalo [{lower_bound_valor:.2f}, {upper_bound_valor:.2f}]):")
        print(outliers_valor[['ID_Cliente', 'Valor_Compra']])
    else:
        print("Nenhum outlier significativo detectado na coluna 'Valor_Compra' pelo método IQR.")

    # Verificação de valores logicamente impossíveis (valor de compra negativo ou zero)
    if df['Valor_Compra'].min() <= 0:
        print(f"**ALERTA**: Valor de Compra mínimo ({df['Valor_Compra'].min():.2f}) é zero ou negativo, o que é um valor inesperado.")
    print("-" * 50)

    # --- Análise de 'Data_Compra' ---
    print("\nAnálise da Coluna: Data_Compra")
    # Converter para datetime para permitir comparações de data
    df['Data_Compra'] = pd.to_datetime(df['Data_Compra'], format='%d/%m/%Y')
    
    current_date = datetime.now()
    future_dates = df[df['Data_Compra'] > current_date]

    if not future_dates.empty:
        print("**ALERTA**: Datas de compra no futuro detectadas:")
        print(future_dates[['ID_Cliente', 'Data_Compra']])
    else:
        print("Nenhuma data de compra no futuro detectada.")
    
    # Verificar o intervalo de datas
    print(f"Data de Compra mais Antiga: {df['Data_Compra'].min().strftime('%d/%m/%Y')}")
    print(f"Data de Compra mais Recente: {df['Data_Compra'].max().strftime('%d/%m/%Y')}")
    print("-" * 50)

    # --- Análise de Colunas Categóricas (re-verificação para surpresas) ---
    print("\nAnálise de Colunas Categóricas:")
    print("Valores únicos para 'Localização':", df['Localização'].unique())
    print("Valores únicos para 'Canal_Aquisição':", df['Canal_Aquisição'].unique())
    print("Valores únicos para 'Produto':", df['Produto'].unique())
    print("Estas colunas parecem consistentes e sem valores fora do esperado com base nas categorias presentes.")
    print("-" * 50 + "\n")

    print("\n--- RESUMO GERAL ---")
    if outliers_idade.empty and outliers_valor.empty and future_dates.empty and df['Idade'].min() > 0 and df['Valor_Compra'].min() > 0:
        print("Com base na análise, não foram encontrados valores significativamente fora do esperado (outliers ou inconsistências lógicas óbvias).")
    else:
        print("Foram identificados alguns valores fora do esperado. Por favor, revise os ALERTA(s) acima para detalhes.")


except FileNotFoundError:
    print(f"Erro")