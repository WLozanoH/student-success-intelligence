import pandas as pd

from src.ingestion.normalize_columns import normalize_column_names

# ============================================================
# FEATURE TYPE CLASSIFICATION
# ============================================================

VARIABLE_TYPE_MAPPING = {
    "categorical": "categorical",
    "binary": "categorical",
    "ordinal": "ordinal",
    "continuous": "numerical",
    "integer": "numerical",
    "count": "numerical",
    "target": "target"
}

REQUIRED_DICTIONARY_COLUMNS = {         # Columnas requeridas en el diccionario para la comprobación
    "column_name",
    "variable_type"
}

def classify_feature_types(
    df: pd.DataFrame,               # el primer y segundo parámetro debe ser un dataframe
    dictionary: pd.DataFrame
) -> dict[str, list[str]]:          # el retorno es un diccionario, donde la clave es un str, y el valor es una lista de str
    """
    Clasifica las variables del dataset según su naturaleza 
    semántica definida en el diccionario de datos
    
    Groups:
    - categorical
    - ordinal
    - numerical
    - target
    
    Parameters:
    ----------
    df: pd.DataFrame
        Dataset que se desea clasificar
        
    dictionary: pd.DataFrame
        Diccionario de datos con las columnas:
        column_name, variable_type
        
    Returns:
    -------
    dict[str, list[str]]
        Diccionario con los nombres de las variables
        agrupadas según su naturaleza semántica.
        
    Raises:
    ------
    TypeError
        Si las entradas no son DataFrames
        
    ValueError
        Si existen columnas sin metadatos, tipos desconocidos
        o nombres de columnas duplicados.
    """
    
    df = normalize_column_names(df)     # Normalizacion de los nombres de las columnas dataframe(quita los espacios, tabulaciones.)
    
    
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            'El dataset debe ser un pandas DataFrame.'
        )
        
    if not isinstance(dictionary, pd.DataFrame):
        raise TypeError(
            'El diccionario debe ser un pandas DataFrame.'
        )
        
    if df.columns.duplicated().any():
        raise ValueError(
            'El dataset contiene nombres de columnas duplicados'
        )
        
    if dictionary.columns.duplicated().any():
        raise ValueError(
            'El diccionario contiene nombres de columnas duplicados'
        )
        
    
    if not REQUIRED_DICTIONARY_COLUMNS.issubset(                # Se lee: si las columnas requeridas del diccionario, no se encuentran en los nombre del csv diccionario
        dictionary.columns
    ):
        raise ValueError(
            'El diccionario debe contener las columnas: '
            'column_name y variable_type'
        )
        
    if dictionary["column_name"].duplicated().any():
        raise ValueError(
            'El diccionario contiene variables duplicadas'
        )

    metadata = dictionary[                  # extraer del diccionario solo las dos variables a usar
        ["column_name", "variable_type"]
    ].copy()
    
    
    # normalizar los valores de variable_type
    metadata["variable_type"] = (
        metadata["variable_type"]   # convierte los valores de la columna
        .astype("string")       # -> convierte a tipo str
        .str.strip()            # -> elimina espacios
        .str.lower()            # -> todo a minúsculas
    )
    
    # normalizar los valores de column_name
    metadata["column_name"] = (
    metadata["column_name"]
    .astype(str)
    .str.strip()
    .str.lower()
)
    
    # verificar que todas las columnas del dataset 
    # estén documentadas
    
    missing_metadata = (
        set(df.columns) - set(metadata["column_name"])
    )

    # si hay metadata faltante, lanzar error
    if missing_metadata:
        raise ValueError(
            'Faltan variables en el diccionario: '
            f'{sorted(missing_metadata)}'
        )

    # obtener los metadatos correspondientes al dataset
    
    metadata = metadata[
        metadata["column_name"].isin(df.columns)        # confirmar que los valores de column_name en metadata deben estar en los nombres de columnas del df
    ]

    # Identificar tipos semanticos desconocidos
    unknown_types = (
        set(metadata["variable_type"].dropna())         # set: convierte a un conjunto de valores únicos.
        - set(VARIABLE_TYPE_MAPPING)                    # set: cuando se utiliza un diccionario dentro de set, sólo obtiene sus claves.
    )
    
    # lanzar error si hay tipos de datos desconocidos.
    if unknown_types:
        raise ValueError(
            'Se encontraron tipos de variables no reconocidos: '
            f'sorted{unknown_types}'
    )
        
     
    # si hay valores nulos en variable_type
    if metadata["variable_type"].isna().any():
        raise ValueError(
            'Existen variables sin tipo semántico definido'
        )   
        
    # Inicializar los grupos
    features_groups = {
        "categorical": [],
        "ordinal": [],
        "numerical": [],
        "target": []
    }
    
    # iterar por filas para clasificar 
    for _, row in metadata.iterrows():
        
        column = row["column_name"]
        variable_type = row["variable_type"]
        
        # Usar el mapeo de diccionario
        group = VARIABLE_TYPE_MAPPING[variable_type]        # cada tipo de dato semantico, regresa estandarizado a su grupo correspondiente
        
        # Añadir las variables al diccionario nuevo de features
        features_groups[group].append(column)
        
    return features_groups