import pandas as pd
import numpy as np

import pandas as pd

def remover_linhas_colunas_vazias(dataframe):
    """
    Remove linhas e colunas vazias de um DataFrame.
    Args:
        dataframe (pandas.DataFrame): O DataFrame a ser limpo.
    Returns:
        pandas.DataFrame: O DataFrame sem as linhas e colunas vazias.
    Exemplo:
        >>> df = pd.DataFrame({'A': [1, 2, None, 4],
                               'B': [None, None, None, None],
                               'C': [7, None, 9, 10]})
        >>> remover_linhas_colunas_vazias(df)
           A     C
        0  1   7.0
        1  2   NaN
        2  4   9.0
        3  5  10.0
    """
    empty_rows = dataframe.index[dataframe.isnull().all(axis=1)]
    empty_cols = dataframe.columns[dataframe.isnull().all(axis=0)]
    df_clean = dataframe.drop(empty_rows, axis=0).drop(empty_cols, axis=1)
    return df_clean
