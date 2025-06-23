import pandas as pd

# Define o caminho completo para o seu arquivo CSV.
# Ajuste este caminho se necessário.
file_path = r'C:\Users\hector.dallacosta\Downloads\Dataset questão 1.csv' 

try:
    # Carregar o dataset com o delimitador e codificação corretos.
    df = pd.read_csv(file_path, delimiter=';', encoding='utf-8-sig')
    print(f"Dataset '{file_path}' carregado com sucesso para análise de compras exageradas.\n")

    print("--- Verificação de Compras Exageradamente Altas ou Baixas (Outliers em Valor_Compra) ---\n")

    # --- Análise de 'Valor_Compra' para Outliers (IQR Method) ---
    print("Análise da Coluna: Valor_Compra")
    print(f"Valor Mínimo de Compra: R$ {df['Valor_Compra'].min():.2f}")
    print(f"Valor Máximo de Compra: R$ {df['Valor_Compra'].max():.2f}")

    # Calcular Q1 (1º quartil), Q3 (3º quartil) e IQR (Intervalo Interquartil)
    Q1_valor = df['Valor_Compra'].quantile(0.25)
    Q3_valor = df['Valor_Compra'].quantile(0.75)
    IQR_valor = Q3_valor - Q1_valor

    # Definir os limites para identificação de outliers
    # Valores abaixo de Q1 - 1.5*IQR são considerados 'exageradamente baixos'
    # Valores acima de Q3 + 1.5*IQR são considerados 'exageradamente altos'
    lower_bound_valor = Q1_valor - 1.5 * IQR_valor
    upper_bound_valor = Q3_valor + 1.5 * IQR_valor

    print(f"\nPrimeiro Quartil (Q1): R$ {Q1_valor:.2f}")
    print(f"Terceiro Quartil (Q3): R$ {Q3_valor:.2f}")
    print(f"Intervalo Interquartil (IQR): R$ {IQR_valor:.2f}")
    print(f"Limite Inferior para Outliers: R$ {lower_bound_valor:.2f}")
    print(f"Limite Superior para Outliers: R$ {upper_bound_valor:.2f}")

    # Identificar os outliers
    outliers_valor = df[(df['Valor_Compra'] < lower_bound_valor) | (df['Valor_Compra'] > upper_bound_valor)]

    if not outliers_valor.empty:
        print(f"\n**ALERTA**: Foram detectados clientes com compras exageradamente altas ou baixas (outliers) na coluna 'Valor_Compra'.")
        print("Estes valores estão fora do intervalo considerado 'normal' com base no IQR:")
        print(outliers_valor[['ID_Cliente', 'Valor_Compra']].sort_values(by='Valor_Compra'))
        
        # Classificar os outliers em altos e baixos
        outliers_baixos = outliers_valor[outliers_valor['Valor_Compra'] < lower_bound_valor]
        outliers_altos = outliers_valor[outliers_valor['Valor_Compra'] > upper_bound_valor]

        if not outliers_baixos.empty:
            print("\nCompras Exageradamente Baixas (abaixo de R$ {:.2f}):".format(lower_bound_valor))
            print(outliers_baixos[['ID_Cliente', 'Valor_Compra']])
        if not outliers_altos.empty:
            print("\nCompras Exageradamente Altas (acima de R$ {:.2f}):".format(upper_bound_valor))
            print(outliers_altos[['ID_Cliente', 'Valor_Compra']])

    else:
        print("Nenhum cliente detectado com compras exageradamente altas ou baixas (nenhum outlier significativo) pelo método IQR.")
    print("-" * 50 + "\n")

except FileNotFoundError:
    print(f"Erro: O arquivo '{file_path}' não foi encontrado. Por favor, verifique o nome e o caminho completo do arquivo.")
except PermissionError:
    print(f"Erro de permissão: Não foi possível acessar o arquivo ou diretório '{file_path}'.")
    print("Verifique se o arquivo não está aberto em outro programa e se você tem permissões.")
except UnicodeDecodeError as e:
    print(f"Erro de decodificação: Ocorreu um problema ao ler o arquivo com a codificação especificada. Mensagem: {e}")
    print("A codificação 'utf-8-sig' é geralmente a correta para este arquivo. Se o erro persistir, o arquivo pode estar em outra codificação.")
except KeyError as e:
    print(f"Erro: A coluna {e} não foi encontrada no DataFrame. Verifique a grafia do nome da coluna ou o conteúdo do arquivo CSV.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")