
import pandas as pd


# ============================================================
# MISSING VALUE ANALYSIS
# ============================================================

def analyze_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analiza los valores faltantes de cada columna del dataset.

    Calcula:
    - Cantidad de valores faltantes.
    - Porcentaje de valores faltantes.
    - Cantidad de valores disponibles.
    - Indicador de necesidad de tratamiento.

    La función no modifica el DataFrame original ni realiza
    imputaciones.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset que se desea analizar.

    Returns
    -------
    pd.DataFrame
        Reporte de valores faltantes por columna.

    Raises
    ------
    TypeError
        Si la entrada no es un pandas DataFrame.

    ValueError
        Si el DataFrame está vacío o tiene columnas duplicadas.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "La entrada debe ser un pandas DataFrame."
        )

    if df.empty:
        raise ValueError(
            "No se puede analizar un DataFrame vacío."
        )

    if df.columns.duplicated().any():
        raise ValueError(
            "El DataFrame contiene nombres de columnas duplicados."
        )

    # Contabilizar valores faltantes por columna.
    missing_count = df.isna().sum()

    # Calcular porcentaje de valores faltantes.
    missing_percentage = (
        df.isna().mean() * 100
    )

    # Contabilizar valores disponibles.
    non_missing_count = df.notna().sum()

    # Construir el reporte.
    report = pd.DataFrame({
        "column_name": df.columns,
        "missing_count": missing_count.values,
        "missing_percentage": missing_percentage.values,
        "non_missing_count": non_missing_count.values,
        "data_type": [
            str(df[column].dtype)
            for column in df.columns
        ],
        "requires_treatment": (
            missing_count.values > 0
        )
    })

    # redondear a 2 decimales
    report["missing_percentage"] = (
        report["missing_percentage"].round(2)
    )

    return report
