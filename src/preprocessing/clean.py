
import pandas as pd


# ============================================================
# DATA CLEANING
# ============================================================

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica reglas básicas de limpieza al conjunto de datos.

    Transformaciones:
    - Elimina espacios innecesarios en valores de texto.
    - Convierte cadenas vacías en valores faltantes.
    - Conserva las columnas y los registros originales.
    - No modifica el DataFrame de entrada.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset original extraído y validado.

    Returns
    -------
    pd.DataFrame
        Copia del dataset con limpieza básica aplicada.

    Raises
    ------
    TypeError
        Si la entrada no es un DataFrame.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "La entrada debe ser un pandas DataFrame."
        )

    # Crear una copia para preservar el DataFrame original.
    cleaned_df = df.copy(deep=True)

    # Identificar columnas de tipo texto.
    text_columns = cleaned_df.select_dtypes(
        include=["object", "string"]
    ).columns

    # Limpiar espacios y convertir cadenas vacías en NA.
    for column in text_columns:

        cleaned_df[column] = (  
            cleaned_df[column]  # selecciona cada columna del nuevo DataFrame
            .str.strip()
            .replace("", pd.NA)
        )

    return cleaned_df
