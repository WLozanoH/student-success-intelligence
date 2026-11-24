import pandas as pd

from src.config.settings import DOCS_DATA_DIR       # ruta donde se encuentra .../docs

from src.ingestion.extract import extract_dataset   # funcion para extraer el dataset y validarlo



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
        "Marital status": {
        "description": "Student's marital status at enrollment.",
        "variable_type": "categorical",
        "data_group": "demographic",
        "domain": "1=single, 2=married, 3=widower, 4=divorced, 5=facto union, 6=legally separated.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Application mode": {
        "description": "Admission pathway or application mode used by the student.",
        "variable_type": "categorical",
        "data_group": "admission",
        "domain": "Categorical admission codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Application order": {
        "description": "Preference order of the selected course during application.",
        "variable_type": "ordinal",
        "data_group": "admission",
        "domain": "Integer code from 0 to 9; 0 represents first choice and 9 last choice.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Course": {
        "description": "Undergraduate degree program in which the student enrolled.",
        "variable_type": "categorical",
        "data_group": "academic",
        "domain": "Institutional course codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Daytime/evening attendance": {
        "description": "Study schedule selected by the student.",
        "variable_type": "binary",
        "data_group": "academic",
        "domain": "1=daytime, 0=evening.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Previous qualification": {
        "description": "Highest previous educational qualification of the student.",
        "variable_type": "categorical",
        "data_group": "academic_background",
        "domain": "Educational qualification codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Previous qualification (grade)": {
        "description": "Grade obtained in the student's previous qualification.",
        "variable_type": "continuous",
        "data_group": "academic_background",
        "domain": "Grade between 0 and 200.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Nacionality": {
        "description": "Nationality of the student.",
        "variable_type": "categorical",
        "data_group": "demographic",
        "domain": "Nationality codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Mother's qualification": {
        "description": "Highest educational qualification of the student's mother.",
        "variable_type": "categorical",
        "data_group": "family_background",
        "domain": "Educational qualification codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Father's qualification": {
        "description": "Highest educational qualification of the student's father.",
        "variable_type": "categorical",
        "data_group": "family_background",
        "domain": "Educational qualification codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Mother's occupation": {
        "description": "Occupational category of the student's mother.",
        "variable_type": "categorical",
        "data_group": "family_background",
        "domain": "Occupational codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Father's occupation": {
        "description": "Occupational category of the student's father.",
        "variable_type": "categorical",
        "data_group": "family_background",
        "domain": "Occupational codes documented by UCI.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Admission grade": {
        "description": "Grade obtained by the student during the admission process.",
        "variable_type": "continuous",
        "data_group": "admission",
        "domain": "Grade between 0 and 200.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Displaced": {
        "description": "Indicates whether the student is displaced from their usual residence.",
        "variable_type": "binary",
        "data_group": "socioeconomic",
        "domain": "1=yes, 0=no.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Educational special needs": {
        "description": "Indicates whether the student has special educational needs.",
        "variable_type": "binary",
        "data_group": "student_profile",
        "domain": "1=yes, 0=no.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Debtor": {
        "description": "Indicates whether the student has outstanding debt.",
        "variable_type": "binary",
        "data_group": "financial",
        "domain": "1=yes, 0=no.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Tuition fees up to date": {
        "description": "Indicates whether tuition fees are up to date.",
        "variable_type": "binary",
        "data_group": "financial",
        "domain": "1=yes, 0=no.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Gender": {
        "description": "Gender code recorded for the student.",
        "variable_type": "binary",
        "data_group": "demographic",
        "domain": "1=male, 0=female.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Scholarship holder": {
        "description": "Indicates whether the student is a scholarship holder.",
        "variable_type": "binary",
        "data_group": "financial",
        "domain": "1=yes, 0=no.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Age at enrollment": {
        "description": "Age of the student at the time of enrollment.",
        "variable_type": "integer",
        "data_group": "demographic",
        "domain": "Age expressed in years.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "International": {
        "description": "Indicates whether the student is an international student.",
        "variable_type": "binary",
        "data_group": "demographic",
        "domain": "1=yes, 0=no.",
        "availability_stage": "enrollment",
        "prediction_scenario": "enrollment",
    },

    "Curricular units 1st sem (credited)": {
        "description": "Number of curricular units credited in the first semester.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of credited curricular units.",
        "availability_stage": "first_semester",
        "prediction_scenario": "first_semester",
    },

    "Curricular units 1st sem (enrolled)": {
        "description": "Number of curricular units enrolled in the first semester.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of enrolled curricular units.",
        "availability_stage": "first_semester",
        "prediction_scenario": "first_semester",
    },

    "Curricular units 1st sem (evaluations)": {
        "description": "Number of evaluations in the first semester.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of evaluations.",
        "availability_stage": "first_semester",
        "prediction_scenario": "first_semester",
    },

    "Curricular units 1st sem (approved)": {
        "description": "Number of curricular units approved in the first semester.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of approved curricular units.",
        "availability_stage": "first_semester",
        "prediction_scenario": "first_semester",
    },

    "Curricular units 1st sem (grade)": {
        "description": "Average grade obtained in the first semester.",
        "variable_type": "continuous",
        "data_group": "academic_performance",
        "domain": "Grade between 0 and 20.",
        "availability_stage": "first_semester",
        "prediction_scenario": "first_semester",
    },

    "Curricular units 1st sem (without evaluations)": {
        "description": "Number of curricular units without evaluations in the first semester.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of curricular units.",
        "availability_stage": "first_semester",
        "prediction_scenario": "first_semester",
    },

    "Curricular units 2nd sem (credited)": {
        "description": "Number of curricular units credited in the second semester.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of credited curricular units.",
        "availability_stage": "second_semester",
        "prediction_scenario": "second_semester",
    },

    "Curricular units 2nd sem (enrolled)": {
        "description": "Number of curricular units enrolled in the second semester.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of enrolled curricular units.",
        "availability_stage": "second_semester",
        "prediction_scenario": "second_semester",
    },

    "Curricular units 2nd sem (evaluations)": {
        "description": "Number of evaluations in the second semester.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of evaluations.",
        "availability_stage": "second_semester",
        "prediction_scenario": "second_semester",
    },

    "Curricular units 2nd sem (approved)": {
        "description": "Number of curricular units approved in the second semester.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of approved curricular units.",
        "availability_stage": "second_semester",
        "prediction_scenario": "second_semester",
    },

    "Curricular units 2nd sem (grade)": {
        "description": "Average grade obtained in the second semester.",
        "variable_type": "continuous",
        "data_group": "academic_performance",
        "domain": "Grade between 0 and 20.",
        "availability_stage": "second_semester",
        "prediction_scenario": "second_semester",
    },

    "Curricular units 2nd sem (without evaluations)": {
        "description": "Number of curricular units without evaluations in the second semester.",
        "variable_type": "count",
        "data_group": "academic_performance",
        "domain": "Non-negative count of curricular units.",
        "availability_stage": "second_semester",
        "prediction_scenario": "second_semester",
    },

    "Unemployment rate": {
        "description": "Unemployment rate associated with the period represented in the dataset.",
        "variable_type": "continuous",
        "data_group": "macroeconomic",
        "domain": "Percentage; reference period and geographic scope should be verified.",
        "availability_stage": "enrollment_context",
        "prediction_scenario": "enrollment",
    },

    "Inflation rate": {
        "description": "Inflation rate associated with the period represented in the dataset.",
        "variable_type": "continuous",
        "data_group": "macroeconomic",
        "domain": "Percentage; reference period and geographic scope should be verified.",
        "availability_stage": "enrollment_context",
        "prediction_scenario": "enrollment",
    },

    "GDP": {
        "description": "Gross domestic product indicator associated with the period represented in the dataset.",
        "variable_type": "continuous",
        "data_group": "macroeconomic",
        "domain": "Numerical economic indicator; unit and reference period should be verified.",
        "availability_stage": "enrollment_context",
        "prediction_scenario": "enrollment",
    },

    "Target": {
        "description": "Final student outcome: dropout, enrolled, or graduate.",
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