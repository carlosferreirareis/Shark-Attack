import pandas as pd
import numpy as np

def unica_cel_preenchida_lin_col(df):
    """
    Identifica todas as linhas e colunas do DataFrame que possuem apenas uma célula preenchida.
    Args:
        df (pandas.DataFrame): O DataFrame a ser verificado.
    Returns:
        tuple: Uma tupla contendo duas listas, uma para as linhas com apenas uma célula preenchida e outra para as colunas com apenas uma célula preenchida.
    Exemplo:
        # Cria um DataFrame de exemplo
        data = {'A': [1, None, 3, None, 5], 'B': [None, None, None, None, 10], 'C': [None, 12, None, None, None]}
        df = pd.DataFrame(data)

        # Chama a função para identificar as linhas e colunas com apenas um valor não nulo
        linhas_unicas, colunas_unicas = identificar_linhas_colunas_unicas(df)

        print("Linhas com apenas um valor não nulo:", linhas_unicas)
        print("Colunas com apenas um valor não nulo:", colunas_unicas)
    """
    # Identifica as linhas com apenas um valor não nulo
    linhas_unicas = df.index[df.count(axis=1) == 1].tolist()

    # Identifica as colunas com apenas um valor não nulo
    colunas_unicas = df.columns[df.count(axis=0) == 1].tolist()

    return print(linhas_unicas, colunas_unicas)