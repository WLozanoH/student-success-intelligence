import pandas as pd

from pandas.api.types import is_numeric_dtype, is_object_dtype

# ============================================================
# ESQUEMA ESPERADO DEL DATASET
# ============================================================

COLUMNAS_ESPERADAS = [
    "Marital status",
    "Application mode",
    "Application order",
    "Course",
    "Daytime/evening attendance",
    "Previous qualification",
    "Previous qualification (grade)",
    "Nacionality",
    "Mother's qualification",
    "Father's qualification",
    "Mother's occupation",
    "Father's occupation",
    "Admission grade",
    "Displaced",
    "Educational special needs",
    "Debtor",
    "Tuition fees up to date",
    "Gender",
    "Scholarship holder",
    "Age at enrollment",
    "International",
    "Curricular units 1st sem (credited)",
    "Curricular units 1st sem (enrolled)",
    "Curricular units 1st sem (evaluations)",
    "Curricular units 1st sem (approved)",
    "Curricular units 1st sem (grade)",
    "Curricular units 1st sem (without evaluations)",
    "Curricular units 2nd sem (credited)",
    "Curricular units 2nd sem (enrolled)",
    "Curricular units 2nd sem (evaluations)",
    "Curricular units 2nd sem (approved)",
    "Curricular units 2nd sem (grade)",
    "Curricular units 2nd sem (without evaluations)",
    "Unemployment rate",
    "Inflation rate",
    "GDP",
    "Target"
]


VALORES_ESPERADOS_TARGET = {
    "Dropout",
    "Enrolled",
    "Graduate"
}


FILAS_ESPERADAS = 4424

TARGET_COLUMN = "Target"

# ============================================================
# VALIDACIÓN DEL ESQUEMA
# ============================================================

def validate_columns(df: pd.DataFrame) -> list[dict]:
    """
    Valida las columnas esperadas del dataset.
    
    Verifica:
    
    - Columnas faltantes.
    - Columnas inesperadas.
    - Nombres de columnas duplicadas.
    """
    
    resultados = [] 
    
    columnas_actuales = list(df.columns)
    
    columnas_faltantes = sorted(
        set(COLUMNAS_ESPERADAS) - set(columnas_actuales)
    )
    
    columnas_inesperadas = sorted(
        set(columnas_actuales) - set(COLUMNAS_ESPERADAS)
    )
    
    columnas_duplicadas = (
        df.columns[df.columns.duplicated()]     # máscara de booleanos para identificar duplicados.
        .unique()     # devuelve valores únicos
        .tolist()     # convierte el objeto Index de pandas en una lista nativa de Python.
    )
    
    resultados.append({
        "Verificar": "Columnas faltantes",
        "Estado": "FAIL" if columnas_faltantes else "PASS",
        "Detalles": (
            ", ".join(columnas_faltantes)
            if columnas_faltantes else "No hay columnas faltantes"
        ),
        "Filas_afectadas": 0,
        "Columnas_afectadas": len(columnas_faltantes)
    })
    
    resultados.append({
        "Verificar": "Columnas inesperadas",
        "Estado": "FAIL" if columnas_inesperadas else "PASS",
        "Detalles": (
            ", ".join(columnas_inesperadas)
            if columnas_inesperadas else "No hay columnas inesperadas"
        ),
        "Filas_afectadas": 0,
        "Columnas_afectadas": len(columnas_inesperadas)
    })
    
    resultados.append({
        "Verificar": "Columnas duplicadas",
        "Estado": "FAIL" if columnas_duplicadas else "PASS",
        "Detalles": (
            ", ".join(columnas_duplicadas)
            if columnas_duplicadas else "No hay columnas duplicadas"
        ),
        "Filas_afectadas": 0,
        "Columnas_afectadas": len(columnas_duplicadas)
    })
    
    return resultados


def validate_data_types(df: pd.DataFrame) -> list[dict]:
    """
    Valida los tipos de datos de las columnas del dataset.
    
    Todas las variables predictoras deben ser numéricas.
    La variable objetivo debe ser categórica
    """
    resultados = []
    
    for column in COLUMNAS_ESPERADAS:
        if column not in df.columns or df.columns.tolist().count(column) > 1:
            continue           # abandona la iteracción actual y pasa directamente a la siguiente.
        
        series = df[column]
        
        if column == TARGET_COLUMN:
            valid_type = (                                          # almacenará un valor booleano(True/False)
                is_object_dtype(series.dtype)                       # Compueba si el tipo de dato de la serie es "objeto"
                or isinstance(series.dtype, pd.CategoricalDtype)    # insisntance(objeto, tipo), comprueba si el objeto pertenece a un tipo determinado. En este caso de tipo categórico de pandas
                or isinstance(series.dtype, pd.StringDtype)         # verifica si el objeto evaluado es de tipo string(cadena)
            )                                                       # Si cumple alguna condición, devolverá True.

        else: 
            
            valid_type = is_numeric_dtype(series.dtype)             # Comprueba si la serie es de tipo numérico.
            
        resultados.append({
            "Verificar": "Tipo de dato",
            "Columna": column,
            "Estado": "PASS" if valid_type else "FAIL",
            "Detalles": (
                f'Tipo esperado correctamente detectado {series.dtype}'
                if valid_type
                else (
                    f'Tipo inesperado {series.dtype}.'
                    f'Esperado {'Categórica' if column == TARGET_COLUMN else 'numerica'}'
                )
            ),
            "Filas_afectadas": 0,
            "Columnas_afectadas": 0 if valid_type else 1
        })

    return resultados


def validate_row_count(df: pd.DataFrame) -> list[dict]:
    """"
    Valida el número de registros esperados del Dataset.
    
    Se notifica una cantidad de filas diferente a modo de advertencia,
    ya que futuras versiones del conjunto de datos podrían contener nuevos registros.
    """
    
    filas_actuales = len(df)
    
    cantidad_validada = filas_actuales == FILAS_ESPERADAS
    
    return [{
        "Verificar": "Cantidad de filas esperadas",
        "Estado": "PASS" if cantidad_validada else "WARNING",
        "Detalles": (
            f'Esperado: {FILAS_ESPERADAS} | Actual: {filas_actuales}'
        ),
        "Filas_afectadas": abs(FILAS_ESPERADAS - filas_actuales),
        "Columnas_afectadas": 0
    }]
    

def validate_schema(df: pd.DataFrame) -> list[dict]:
    """
    Ejecuta todas las comprobaciones de validación de esquema.
    
    Retorna una lista consolidada de los resultados de validación.
    """
    
    resultados = []                                 # Lista vacía, donde se guardarán los resultados.
                                                    # .extend(): es un método de listas de Python. Su función es agregar los elementos de un iterable de foma individual.
    resultados.extend(validate_columns(df))         # Los resultados de ésta lista, se agregan a la siguiente y así sucesivamente.
    resultados.extend(validate_data_types(df))
    resultados.extend(validate_row_count(df))
    
    return resultados