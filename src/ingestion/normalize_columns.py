
import pandas as pd


# ============================================================
# COLUMN NAME NORMALIZATION
# ============================================================

def normalize_column_names(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Normaliza los nombres de las columnas del dataset.

    Transformaciones:
    - Elimina espacios en blanco al principio y al final.
    - Elimina tabulaciones externas.
    - Conserva los nombres originales en cuanto a su contenido.
    - No modifica el DataFrame de entrada.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset cuyos nombres de columnas se desean normalizar.

    Returns
    -------
    pd.DataFrame
        Copia del dataset con nombres de columnas normalizados.

    Raises
    ------
    TypeError
        Si la entrada no es un DataFrame.

    ValueError
        Si la normalización genera nombres duplicados.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "La entrada debe ser un pandas DataFrame."
        )

    normalized_df = df.copy(deep=True)

    normalized_df.columns = [
        column.strip().lower() 
        if isinstance(column, str) else column           
        for column in normalized_df.columns              
    ]

    if normalized_df.columns.duplicated().any():
        raise ValueError(
            "La normalización produjo nombres de columnas duplicados."
        )

    return normalized_df
