import pandas as pd

from src.validation.schema import (
    COLUMNAS_ESPERADAS,
    validate_columns,
    validate_data_types,
    validate_schema
)


def create_valid_dataset():
    data = {                # DataFrame creado para pruebas de validacion
              column: [0]
              for column in COLUMNAS_ESPERADAS
              if column != "Target"
    }
    
    data["Age at enrollment"] = [20]
    data["Target"] = ["Graduate"]
    
    return pd.DataFrame(data)


def test_valid_columns():       # Pytest busca las funciones que comienzan con "test" y las ejecuta automáticamente
    
    df = create_valid_dataset()
    
    resultados = validate_columns(df)
    
    assert all(                         # all: si todos los elementos evaluados cumplen la condición, devuelve TRUE
        resultado["Estado"] == "PASS"  # Comprueba si el estado de todas las validaciones son PASS
        for resultado in resultados
    )   
    
    
# Se aplica una prueba de comportamiento ante datos inválidos.
def test_missing_column():                          
    
    df = create_valid_dataset()   
                     
    # Se elimina la columna a propósito para generar un error.
    df = df.drop(columns=["Gender"])
    
    resultados = validate_columns(df)
    
    missing_result = next(                          # next: devuelve el primer elemento que encuentre
        resultado for resultado in resultados
        if resultado["Verificar"] == "Columnas faltantes"
    )
    
    # Comprobar que las condiciones de error se cumplan
    assert missing_result["Estado"] == "FAIL"       
    assert "Gender" in missing_result["Detalles"]   
    
    
def test_columns_unexpected():
    
    df = create_valid_dataset()
    
    # Se crea una nueva variable/columna y se le asigna 1
    df["Unexpected_column"] = 1
    
    resultados = validate_columns(df)
    
    # verificar el error
    unexpected_result = next(
        resultado for resultado in resultados
        if resultado["Verificar"] == "Columnas inesperadas"
    )
    
    assert unexpected_result["Estado"] == "FAIL"
    
    
def test_duplicate_columns():
    
    df = create_valid_dataset()
    
    # Duplicar una columna a propósito
    df.columns = [
        "Gender" if i == 0 else column              # coloca "Gender" en el indice 0, el resto, su name column normal.
    for i, column in enumerate(df.columns)          # enumerate: para obtener la posicion y nombre
    ]
    
    resultados = validate_columns(df)
    
    # verificar el error
    duplicate_error = next(
        resultado for resultado in resultados
        if resultado["Verificar"] == "Columnas duplicadas"
    )
    
    # verificar el error
    assert duplicate_error["Estado"] == "FAIL"
    

def test_invalid_data_types():
    
    df = create_valid_dataset()
    
    # Cambiar el valor de una variable numerica a str a propósito
    df["Age at enrollment"] = ["twenty"] # en lugar de [20]
    
    resultados = validate_data_types(df)
    
    invalid_type_result = next(
        resultado for resultado in resultados
        if resultado["Columna"] == "Age at enrollment"      # Distingue Mayusc/Minusc
    )
    
    # verificar si se cumple el error
    assert invalid_type_result["Estado"] == "FAIL"
    

def test_schema_validation_results():

    df = create_valid_dataset()

    resultados = validate_schema(df)        # valida el pipeline de schema(orquesta las funciones anteriores)

    assert isinstance(resultados, list)      # Los resultados deben ser devueltos en una lista
    assert len(resultados) > 0