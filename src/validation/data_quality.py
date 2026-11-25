
import pandas as pd


# ============================================================
# CONFIGURACIÓN DE LA CALIDAD DE LOS DATOS
# ============================================================

TARGET_COLUMN = "Target"

CONTEO_COLUMNAS = [
    f"Curricular units {semester} sem ({metric})"       # Se usa comprensión de listas para que la combinación de ambos bucles nos de todos los nombres.
    for semester in ["1st", "2nd"]
    for metric in [
        "credited",
        "enrolled",
        "evaluations",
        "approved",
        "without evaluations"
    ]
]

SEMESTERS = ["1st", "2nd"]


# ============================================================
# VALIDACION DE LA CALIDAD DE DATOS
# ============================================================

def validate_missing_values(df: pd.DataFrame) -> list[dict]:
    """
    Detecta valores faltantes en las columnas del dataset.

    Los valores faltantes se notifican como Warning, porque
    su tratamiento forma parte de la preparación de datos.
    """

    resultados = []

    conteo_faltantes = df.isna().sum()

    for columna, cantidad in conteo_faltantes.items():

        if cantidad == 0:      # Ignorar columnas sin faltantes. 
            continue            # rompe el bucle y pasa al siguiente.

        resultados.append({
            "Verifica": f"Valores faltantes: {columna}",
            "Estado": "WARN",
            "Detalles": f"{cantidad} valores faltantes detectados",
            "Filas_afectadas": int(cantidad),
            "Columnas_afectadas": 1
        })

    if not resultados:                                      # Si no encontramos faltantes - > if not resultados = vacío
        resultados.append({
            "Verificar": "Valores faltantes",
            "Estado": "PASS",
            "Detalles": "No hay valores faltantes detectados",
            "Filas_afectadas": 0,
            "Columnas_afectadas": 0
        })

    return resultados


def validate_duplicate_records(df: pd.DataFrame) -> list[dict]:
    """
    Detectar registros completamente duplicados.

    Los registros duplicados son notificados como advertencias.
    """

    cantidad_duplicados = int(df.duplicated().sum())

    return [{
        "Verificar": "Registros duplicados",
        "Estado": "WARN" if cantidad_duplicados > 0 else "PASS",
        "Detalles": (
            f"{cantidad_duplicados} Registros duplicados detectados"
        ),
        "Filas_afectadas": cantidad_duplicados,
        "Columnas_afectadas": 0
    }]


def validate_target_values(df: pd.DataFrame) -> list[dict]:
    """
    Valida las categorias permitidas de la variable objetivo.
    """

    if TARGET_COLUMN not in df.columns:
        return []

    valores_esperados = {
        "Dropout",
        "Enrolled",
        "Graduate"
    }

    valores_actuales = set(
        df[TARGET_COLUMN].dropna().unique()
    )

    valores_inesperados = valores_actuales - valores_esperados

    return [{
        "Verificar": "Valores permitidos del objetivo",
        "Estado": "FAIL" if valores_inesperados else "PASS",
        "Detalles": (
            f"Valores_inesperados: {sorted(valores_inesperados)}"
            if valores_inesperados
            else "Todos los valores del objetivo son válidos."
        ),
        "Filas_afectadas": int(
            df[TARGET_COLUMN].isin(valores_inesperados).sum()
        ),
        "Columnas_afectadas": 1 if valores_inesperados else 0
    }]


def validate_negative_counts(df: pd.DataFrame) -> list[dict]:
    """
    Detectar valores negativos en las columnas de recuento de unidades curriculares.
    """

    results = []

    for column in CONTEO_COLUMNAS:

        if column not in df.columns:                    # Si la columna no exista, pasa a la siguiente.
            continue

        invalid_mask = df[column] < 0                   # máscara booleana, devuelve TRUE/FALSE
                                                        # nos permite identificar que filas cumplen una condición.
        invalid_count = int(invalid_mask.sum())         # Contar los registros incorrectos.

        results.append({
            "Verificar": f"Valores negativos: {column}",
            "Estado": "FAIL" if invalid_count else "PASS",
            "Detalles": (
                f"{invalid_count} Valores negativos detectados"
            ),
            "Filas_afectadas": invalid_count,
            "Columnas_afectadas": 1 if invalid_count else 0
        })

    return results


def validate_age(df: pd.DataFrame) -> list[dict]:
    """
    Valida que la edad de los estudiantes sea positiva.
    """

    column = "Age at enrollment"

    if column not in df.columns:
        return []

    invalid_mask = df[column].notna() & (df[column] <= 0)       # Solo edades registradas y que sean 0 o negativas.

    invalid_count = int(invalid_mask.sum())                     # Cuenta los registros que cumplen la condicion.

    return [{
        "Verificar": "Edad de inscripción positiva",
        "Estado": "FAIL" if invalid_count else "PASS",
        "Detalles": (
            f"{invalid_count} valores de edad inválidos"
        ),
        "Filas_afectadas": invalid_count,
        "Columnas_afectadas": 1 if invalid_count else 0
    }]


def validate_approved_units(df: pd.DataFrame) -> list[dict]:        # La idea es verificar las Unidades aprobadas <= Unidades matriculadas
    """
    Verificar que las unidades curriculares aprobadas no superen
    las unidades curriculares inscritas en ninguno de los semestres.

    Las filas con valores faltantes se excluyen de esta comparación.
    """

    results = []

    for semester in SEMESTERS:

        enrolled = f"Curricular units {semester} sem (enrolled)"
        approved = f"Curricular units {semester} sem (approved)"

        if enrolled not in df.columns or approved not in df.columns:
            continue

        comparable = df[[enrolled, approved]].notna().all(axis=1)

        invalid_mask = (
            comparable
            & (df[approved] > df[enrolled])             # si los aprobados > matriculados, es la condición de máscara inválida
        )

        invalid_count = int(invalid_mask.sum())         # Cuenta los registros que cumplen la condición

        results.append({
            "Verificar": f"Unidades aprobadas <= Unidades matriculadas ({semester} semestre)",
            "Estado": "FAIL" if invalid_count else "PASS",
            "Detalles": (
                f"{invalid_count} registros inconsistentes detectados"
            ),
            "Filas_afectadas": invalid_count,
            "Columnas_afectadas": 2 if invalid_count else 0
        })

    return results


def validate_data_quality(df: pd.DataFrame) -> list[dict]:
    """
    Ejecutar todas las validaciones de calidad de los datos.
    """

    results = []

    results.extend(validate_missing_values(df))
    results.extend(validate_duplicate_records(df))
    results.extend(validate_target_values(df))
    results.extend(validate_negative_counts(df))
    results.extend(validate_age(df))
    results.extend(validate_approved_units(df))

    return results
