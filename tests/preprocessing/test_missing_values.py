import pandas as pd
import pytest

from src.preprocessing.missing_values import analyze_missing_values

def test_missing_values_count():
    """
    Verifica cantidad de valores nulos
    """
    
    
    df = pd.DataFrame({
        "Age": [20, 15, None],
        "Target": ["Graduate", "Enrolled", "Dropout"]
    })
    
    report = analyze_missing_values(df)
    
    age_result = report.loc[
        report["column_name"] == "Age"
        ].iloc[0]           # busca en la posicion de fila primera
    
    # verificar la condición
    assert age_result["missing_count"] == 1
    

def test_missing_values_percentage():
    """
    Verifica porcentaje de valores nulos
    """
    
    df = pd.DataFrame({
        "Age": [15, 20, None, None]
    })
    
    reporte = analyze_missing_values(df)
    
    # verifica la condición
    assert reporte.loc[0, "missing_percentage"] == 50.00
    
    
def test_non_missing_values_count():
    """
    verifica que cuente los valores disponibles
    """
    
    df = pd.DataFrame({
        "Age": [20, None, 25]
    })
    
    reporte = analyze_missing_values(df)
    
    # verificar los valores disponibles
    assert reporte.loc[0, "non_missing_count"] == 2
    

def test_columns_requiring_treatment():
    """
    Verifica las columnas que requieren tratamiento
    """
    
    df = pd.DataFrame({
        "Age": [25, None, None],
        "Target": ["Graduate", "Enrolled", "Dropout"]
    })
    
    reporte = analyze_missing_values(df)
    
    age_result = reporte.loc[               # devuelve una serie
        reporte["column_name"] == "Age"
        ].iloc[0]                           # devuelve solo el booleano
    
    target_result = reporte.loc[
        reporte["column_name"] == "Target"   
    ].iloc[0]
    
    # verificar la condición    
    assert age_result["requires_treatment"] == True     ## dos booleanos se pueden comparar
    assert target_result["requires_treatment"] == False
    
    
def test_no_missing_values():
    """
    verificar que no haya valores nulos
    """
    
    df = pd.DataFrame({
        "Age": [20, 22, 25],
        "Target": ["Graduate", "Dropout", "Enrolled"]
    })
    
    reporte = analyze_missing_values(df)
    
    # verificar condicion
    assert reporte["missing_count"].sum() == 0
    assert not reporte["requires_treatment"].any()
    
    
def test_original_dataframe_is_not_modified():

    df = pd.DataFrame({
        "Age": [20, None, 25]
    })

    original_df = df.copy(deep=True)

    analyze_missing_values(df)

    pd.testing.assert_frame_equal(df, original_df)    
    
    
    
def test_non_dataframe_input_raises_error():

    with pytest.raises(TypeError):

        analyze_missing_values([20, 25, 30])
            
    
    
def test_empty_dataframe_raises_error():
    """
    Verifica lanzar un error cuando 
    el DataFrame esté vacío.
    """
    
    df = pd.DataFrame()
    
    with pytest.raises(ValueError):
        
        analyze_missing_values(df)


def test_duplicate_columns_raise_error():

    df = pd.DataFrame(
        [[20, 25]],
        columns=["Age", "Age"]
    )

    with pytest.raises(ValueError):

        analyze_missing_values(df)