from pathlib import Path
import pandas as pd
from src.config.settings import (
    RAW_DATA_FILE,
    PROJECT_ROOT
)

def extract_dataset(
    file_path: str | Path = RAW_DATA_FILE,
    sep: str = ";",
    encoding: str = 'utf-8'
) -> pd.DataFrame:
    """Extrae el conjunto de datos original de los estudiantes de un archivo CSV.
    
    Parametros:
    file_path: str | Path
        Localizacion fuente del archivo CSV.
    
    sep: str
        Delimitador CSV.
    
    encoding: str
        codificación del archivo. por defecto utf-8.
    
    Returns
    -------
    pd.DataFrame
        Dataset extraído sin transformaciones de datos.
    
    Raises
    -------
    FileNotFoundError
        Si la fuente del archivo no existe.
        
    ValueError
        Si el dataset extraído está vacío o se ha analizado incorrectamente.
    """
    
    path = Path(file_path)
    
    if not path.is_absolute(): # verificar la raiz del proyecto
        path = PROJECT_ROOT / path
        
    if not path.exists():   # verificar que el archivo exista
        raise FileNotFoundError(
            f'Dataset no encontrado: {path}'
        )
        
    try:    # manejo de excepciones al cargar el dataset
        df = pd.read_csv(
            path,
            sep=sep,
            encoding=encoding
        )
        
        df.columns = df.columns.str.strip()     # Eliminar tabulaciones y espacios
        
    except UnicodeDecodeError as error:     # capturar errores de codificación
        raise ValueError(
            f'No se puede decodificar el dataset usando: {encoding}'
        ) from error
        
    except pd.errors.ParserError as error:  # capturar errores de lectura
        raise ValueError(
            f'No se puede analizar el archivo CSV: {path}'
        ) from error 
        
    if df.empty:    # comprobar si el dataframe está vacío
        raise ValueError(
            f'El dataset extraído está vacío'
        )
        
    if len(df.columns) == 1:  # comprobar que se hayan detectado varias columnas
        raise ValueError(
            "Solo una columna fue detectada. "
            "Verifica el delimitador del CSV (sep)."
        )
        
    return df