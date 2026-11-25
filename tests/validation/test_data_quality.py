import pandas as pd

from src.validation.data_quality import (
    validate_missing_values,
    validate_duplicate_records,
    validate_target_values,
    validate_negative_counts,
    validate_age,
    validate_approved_units,
    validate_data_quality           # funcion orquestadora de las demás funciones
)


def test_missing_values_detection():
    
    df = pd.DataFrame({
        "Age at enrollment": [20, None]
    })
    
    resultados = validate_missing_values(df)
    
    results_missing = next(
        resultado for resultado in resultados
        if resultado["Columna"] == "Age at enrollment"
    )
    
    assert results_missing["Estado"] == "WARN"
    assert results_missing["Filas_afectadas"] == 1
    
    
def test_validate_duplicate_records():
    
    df = pd.DataFrame({
        "student_id": [1, 1, 2],
        "grado": [15, 15, 18]
    })

    resultados = validate_duplicate_records(df)
    
    resultados_duplicados = next(
        resultado for resultado in resultados
        if resultado["Verificar"] == "Registros duplicados"
    )
    
    assert resultados_duplicados["Estado"] == "WARN"


def test_validate_target_values():
    
    df = pd.DataFrame({
        "Target": ["Graduate", "Dropout", "Enrolled"]
    })
    
    resultados = validate_target_values(df)
    
    resultados_objetivo = next(
        resultado for resultado in resultados
        if resultado["Verificar"] == "Valores permitidos del objetivo"
    )
    
    # verificar la condición
    assert resultados_objetivo["Estado"] == "PASS"
    
    
def test_negative_curricular_units():
    
    df = pd.DataFrame({
        "Curricular units 1st sem (credited)": [-1]
    })
    
    resultados = validate_negative_counts(df)
    
    resultados_negativos = next(
        resultado for resultado in resultados
        if resultado["Columna"] == "Curricular units 1st sem (credited)"
    )
    
    # verificar la condicion si se cumple
    assert resultados_negativos["Estado"] == "FAIL"
    
    
def test_validate_age():
    
    df = pd.DataFrame({
        "Age at enrollment" : [20, -1]
    }) 
    
    resultados = validate_age(df)
    
    resultados_age = next(
        resultado for resultado in resultados 
        if resultado["Verificar"] == "Edad de inscripción positiva"
    )  
    
    # verificar la condicion
    assert resultados_age["Estado"] == "FAIL"
    
    
def test_aproved_units_exceded_enrolled():
    
    df = pd.DataFrame({
        "Curricular units 1st sem (enrolled)": [5],
        "Curricular units 1st sem (approved)": [8]
    })
    
    resultados = validate_approved_units(df)
    
    resultados_invalidos = next(
        resultado for resultado in resultados
        if resultado["Estado"] == "FAIL"
    )
    
    # verificar la condicion
    assert resultados_invalidos["Filas_afectadas"] == 1
    
    
def test_valid_aproved_units():
    
    df = pd.DataFrame({
        "Curricular units 1st sem (enrolled)": [7],
        "Curricular units 1st sem (approved)": [2]
    })
    
    resultados = validate_approved_units(df)
    
    resultados_validos = next(
        resultado for resultado in resultados
        if resultado["Estado"] == "PASS"
    )
    
    # confirmar la condición
    assert resultados_validos["Filas_afectadas"] == 0