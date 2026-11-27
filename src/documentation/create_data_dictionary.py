import pandas as pd

from src.config.settings import DOCS_DATA_DIR       # ruta donde se encuentra .../docs

from src.ingestion.extract import extract_dataset   # funcion para extraer el dataset y validarlo

from src.ingestion.normalize_columns import normalize_column_names


# ==========================================
# CONFIGURACIÓN DE SALIDA
# ==========================================

ruta_salida = (                 # Su responsabilidad es ejecutar el procedimiento: generar y guardar el diccionario de datos.
        DOCS_DATA_DIR
        / "data_dictionary"
        / "data_dictionary.csv"
)


# ==========================================
# VARIABLE METADATA
# ==========================================

VARIABLE_METADATA = {
    "marital status": {
        "description": "Estado civil del estudiante al momento de la inscripción.",
        "variable_type": "categorical",
        "data_group": "demographic",
        "domain": "1=single, 2=married, 3=widower, 4=divorced, 5=facto union, 6=legally separated.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "application mode": {
        "description": "Vía de acceso o modalidad de solicitud utilizada por el estudiante.",
        "variable_type": "categorical",
        "data_group": "admission",
        "domain": "Categorical admission codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "application order": {
        "description": "Orden de preferencia del curso seleccionado durante la solicitud.",
        "variable_type": "ordinal",
        "data_group": "admission",
        "domain": "Integer code from 0 to 9; 0 represents first choice and 9 last choice.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "course": {
        "description": "Programa de grado en el que el estudiante se ha matriculado.",
        "variable_type": "categorical",
        "data_group": "academic",
        "domain": "Institutional course codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "daytime/evening attendance": {
        "description": "Horario de estudio seleccionado por el alumno.",
        "variable_type": "binary",
        "data_group": "academic",
        "domain": "1=daytime, 0=evening.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "previous qualification": {
        "description": "Máxima titulación académica previa del estudiante.",
        "variable_type": "categorical",
        "data_group": "academic_background",
        "domain": "Educational qualification codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "previous qualification (grade)": {
        "description": "Calificación obtenida en la titulación previa del estudiante.",
        "variable_type": "continuous",
        "data_group": "academic_background",
        "domain": "Grade between 0 and 200.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "nacionality": {
        "description": "Nacionalidad del estudiante.",
        "variable_type": "categorical",
        "data_group": "demographic",
        "domain": "Nationality codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "mother's qualification": {
        "description": "Máximo nivel educativo de la madre del estudiante.",
        "variable_type": "categorical",
        "data_group": "family_background",
        "domain": "Educational qualification codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "father's qualification": {
        "description": "Máximo nivel educativo del padre del estudiante.",
        "variable_type": "categorical",
        "data_group": "family_background",
        "domain": "Educational qualification codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "mother's occupation": {
        "description": "Categoría ocupacional de la madre del estudiante.",
        "variable_type": "categorical",
        "data_group": "family_background",
        "domain": "Occupational codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "father's occupation": {
        "description": "Categoría ocupacional del padre del estudiante.",
        "variable_type": "categorical",
        "data_group": "family_background",
        "domain": "Occupational codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "admission grade": {
        "description": "Calificación obtenida por el estudiante durante el proceso de admisión.",
        "variable_type": "continuous",
        "data_group": "admission",
        "domain": "Grade between 0 and 200.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "displaced": {
        "description": "Indica si el estudiante se encuentra desplazado de su lugar de residencia habitual.",
        "variable_type": "binary",
        "data_group": "socioeconomic",
        "domain": "1=yes, 0=no.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "educational special needs": {
        "description": "Indica si el estudiante tiene necesidades educativas especiales.",
        "variable_type": "binary",
        "data_group": "student_profile",
        "domain": "1=yes, 0=no.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "debtor": {
        "description": "Indica si el estudiante tiene deuda pendiente.",
        "variable_type": "binary",
        "data_group": "financial",
        "domain": "1=yes, 0=no.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "tuition fees up to date": {
        "description": "Indica si el pago de las tasas de matrícula está al día.",
        "variable_type": "binary",
        "data_group": "financial",
        "domain": "1=yes, 0=no.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "gender": {
        "description": "Código de género registrado para el estudiante.",
        "variable_type": "binary",
        "data_group": "demographic",
        "domain": "1=male, 0=female.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "scholarship holder": {
        "description": "Indica si el estudiante es beneficiario de una beca.",
        "variable_type": "binary",
        "data_group": "financial",
        "domain": "1=yes, 0=no.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "age at enrollment": {
        "description": "Edad del estudiante en el momento de la inscripción.",
        "variable_type": "integer",
        "data_group": "demographic",
        "domain": "Age expressed in years.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "international": {
        "description": "Indica si el estudiante es un estudiante internacional.",
        "variable_type": "binary",
        "data_group": "demographic",
        "domain": "1=yes, 0=no.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "curricular units 1st sem (credited)": {
        "description": "Número de unidades curriculares convalidadas en el primer semestre.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of credited curricular units.",
        "availability_stage": "first_semester",
        "prediction_scenario": "first_semester",
    },

    "curricular units 1st sem (enrolled)": {
        "description": "Número de unidades curriculares en las que se ha matriculado en el primer semestre.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of enrolled curricular units.",
        "availability_stage": "first_semester",
        "prediction_scenario": "first_semester",
    },

    "curricular units 1st sem (evaluations)": {
        "description": "Número de evaluaciones en el primer semestre.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of evaluations.",
        "availability_stage": "first_semester",
        "prediction_scenario": "first_semester",
    },

    "curricular units 1st sem (approved)": {
        "description": "Número de unidades curriculares aprobadas en el primer semestre.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of approved curricular units.",
        "availability_stage": "first_semester",
        "prediction_scenario": "first_semester",
    },

    "curricular units 1st sem (grade)": {
        "description": "Nota media obtenida en el primer semestre.",
        "variable_type": "continuous",
        "data_group": "academic_performance",
        "domain": "Grade between 0 and 20.",
        "availability_stage": "first_semester",
        "prediction_scenario": "first_semester",
    },

    "curricular units 1st sem (without evaluations)": {
        "description": "Número de unidades curriculares sin evaluaciones en el primer semestre.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of curricular units.",
        "availability_stage": "first_semester",
        "prediction_scenario": "first_semester",
    },

    "curricular units 2nd sem (credited)": {
        "description": "Número de unidades curriculares convalidadas en el segundo semestre.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of credited curricular units.",
        "availability_stage": "second_semester",
        "prediction_scenario": "second_semester",
    },

    "curricular units 2nd sem (enrolled)": {
        "description": "Número de unidades curriculares en las que se ha matriculado en el segundo semestre.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of enrolled curricular units.",
        "availability_stage": "second_semester",
        "prediction_scenario": "second_semester",
    },

    "curricular units 2nd sem (evaluations)": {
        "description": "Número de evaluaciones en el segundo semestre.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of evaluations.",
        "availability_stage": "second_semester",
        "prediction_scenario": "second_semester",
    },

    "curricular units 2nd sem (approved)": {
        "description": "Número de unidades curriculares aprobadas en el segundo semestre.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of approved curricular units.",
        "availability_stage": "second_semester",
        "prediction_scenario": "second_semester",
    },

    "curricular units 2nd sem (grade)": {
        "description": "Nota media obtenida en el segundo semestre.",
        "variable_type": "continuous",
        "data_group": "academic_performance",
        "domain": "Grade between 0 and 20.",
        "availability_stage": "second_semester",
        "prediction_scenario": "second_semester",
    },

    "curricular units 2nd sem (without evaluations)": {
        "description": "Número de unidades curriculares sin evaluaciones en el segundo semestre.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of curricular units.",
        "availability_stage": "second_semester",
        "prediction_scenario": "second_semester",
    },

    "unemployment rate": {
        "description": "Tasa de desempleo asociada al período representado en el conjunto de datos.",
        "variable_type": "continuous",
        "data_group": "macroeconomic",
        "domain": "Percentage; reference period and geographic scope should be verified.",
        "availability_stage": "enrollment_context",
        "prediction_scenario": "enrollment",
    },

    "inflation rate": {
        "description": "Tasa de inflación asociada al periodo representado en el conjunto de datos.",
        "variable_type": "continuous",
        "data_group": "macroeconomic",
        "domain": "Percentage; reference period and geographic scope should be verified.",
        "availability_stage": "enrollment_context",
        "prediction_scenario": "enrollment",
    },

    "gdp": {
        "description": "Indicador del producto interno bruto asociado al período representado en el conjunto de datos.",
        "variable_type": "continuous",
        "data_group": "macroeconomic",
        "domain": "Numerical economic indicator; unit and reference period should be verified.",
        "availability_stage": "enrollment_context",
        "prediction_scenario": "enrollment",
    },

    "target": {
        "description": "Resultado final del estudiante: abandono, matriculado o graduado.",
        "variable_type": "target",
        "data_group": "academic_outcome",
        "domain": "Dropout, Enrolled, Graduate.",
        "availability_stage": "end_of_program",
        "prediction_scenario": "outcome",
    }
}

# ==========================================
# GENERACIÓN DEL DICCIONARIO DE DATOS
# ==========================================


def create_data_dictionary(df: pd.DataFrame) -> pd.DataFrame:   # la función debe devolver un DataFrame
    """
    Crea un diccionario de datos completo combinando metadatos definidos 
    manualmente e información del dataset detectada automáticamente
    """
    
    # Normalizar el df 
    df = normalize_column_names(df)
    
    
    missing_metadata = set(df.columns) - set(VARIABLE_METADATA)
    extra_metadata = set(VARIABLE_METADATA) - set(df.columns)

    if missing_metadata or extra_metadata:
        raise ValueError("Desajuste entre las columnas y los metadatos."
            f"Missing metadata {missing_metadata}"
            f"Extra metadata {extra_metadata}"
        )

    registros = []
    
    for column in df.columns:
        metadata = VARIABLE_METADATA[column]

        registros.append({
            "column_name": column,
            "description": metadata["description"],
            "data_type": str(df[column].dtype),
            "variable_type": metadata["variable_type"],
            "data_group": metadata["data_group"],
            "domain": metadata["domain"],
            "availability_stage": metadata["availability_stage"],
            "prediction_scenario": metadata["prediction_scenario"],
            "is_target": column == "Target",
            "missing_count": int(df[column].isna().sum()),
            "unique_values": int(df[column].nunique()),
        })
        
    return pd.DataFrame(registros)

def main():
    """
    Extraer el dataset y generar un diccionario de datos
    """
    
    df = extract_dataset()
    
    data_dictionary = create_data_dictionary(df)

    ruta_salida.parent.mkdir(
        parents = True,
        exist_ok = True
    )
    
    data_dictionary.to_csv(
        ruta_salida,
        index=False,
        encoding='utf-8-sig'
    )
    
    print('Diccionario de datos generado existosamente')
    print(f'Ruta de salida: {ruta_salida}')
    print(f'Variables documentadas: {len(data_dictionary)}')

    
    
if __name__ == "__main__":
    main()