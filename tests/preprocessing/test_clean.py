
import pandas as pd
import pytest

from src.preprocessing.clean import clean_dataset


def test_clean_text_values():
    """
    Verifica que limpia correctamente los
    espacios de los valores de las columnas.
    """
    
    
    df = pd.DataFrame({
        "Target": [
            " Graduate ",
            "Dropout  ",
            "   Enrolled"
        ]
    })

    df_cleaned = clean_dataset(df)

    # verificar si cumple la condición
    assert df_cleaned["Target"].tolist() == [
        "Graduate",
        "Dropout",
        "Enrolled"
    ]
    
    
def test_original_is_not_modified():
    """
    Verifica que el DataFrame original
    no es modificado.
    """
    
    
    df = pd.DataFrame({
        "Target": [" Graduate  "]
    })
    
    # hacer la copia del df original
    df_original = df.copy(deep=True)
    
    # limpiar el df 
    clean_dataset(df)
    
    # comparar ambos df
    pd.testing.assert_frame_equal(df, df_original)    
    
    
def test_row_and_column_count_are_preserved():
    """
    Para verificar si la cantidad de filas y columnas
    es igual después de la limpieza.    
    """
    df = pd.DataFrame({
        "Age at enrollment": [20, 22, 25],
        "Target": ["Graduate", "Dropout", "Enrolled"]
    })
    
    cleaned_df = clean_dataset(df)
    
    # verificar la condicion
    assert cleaned_df.shape == df.shape
    
    
def test_non_dataframe_input_raises_error():
    """
    El test lanza un TypeError cuando el parámetro 
    que recibe la función de limpieza no es un df
    """
    
    
    with pytest.raises(TypeError):
        
        clean_dataset(["Graduate", "Dropout"])
    

def test_empty_strings_are_converted_to_missing():
    
    df = pd.DataFrame({
        "Target": [
            "Enrolled",
            " ",
            "Dropout"
        ]
    })

    # limpiar los datos
    cleaned_df = clean_dataset(df)
    
    # verificar que existan valores NA
    assert pd.isna(cleaned_df.loc[1, "Target"]) # verificar en el índice de fila 1, columna "Target" es un valor NA