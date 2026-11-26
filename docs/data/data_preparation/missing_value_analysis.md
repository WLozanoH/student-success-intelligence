# Análisis de valores faltantes

## 1. Objetivo

El objetivo de este módulo es identificar y cuantificar los valores faltantes en el conjunto de datos de estudiantes antes de aplicar cualquier estrategia de imputación.

El análisis proporciona información a nivel de columna para fundamentar futuras decisiones de preprocesamiento.

## 2. Módulo

`src/preprocessing/missing_values.py`

Función principal:

`analyze_missing_values(df: pd.DataFrame) -> pd.DataFrame`

## 3. Métricas de análisis

| Métrica | Descripción |
|---|---|
| column_name | Nombre de la columna analizada. |
| missing_count | Número de valores faltantes. |
| missing_percentage | Porcentaje de valores faltantes respecto al número total de registros. |
| non_missing_count | Número de valores presentes. |
| data_type | Tipo de dato actual en pandas. |
| requires_treatment | Indica si la columna contiene valores faltantes. |

## 4. Política de tratamiento

El módulo no realiza imputaciones automáticas ni elimina registros.

Las decisiones sobre el tratamiento de los valores faltantes deben considerar:

- El tipo de variable y su significado semántico.
- El porcentaje de valores faltantes.
- Las posibles causas de la ausencia de datos.
- El impacto en el escenario predictivo.
- El riesgo de fuga de información (*data leakage*).

Si fuera necesaria una imputación para el modelado predictivo, los parámetros de imputación deben ajustarse utilizando únicamente los datos de entrenamiento.

## 5. Pruebas

Pruebas automatizadas:

`tests/preprocessing/test_missing_values.py`

Ejecución:

```bash
python -m pytest tests/preprocessing/test_missing_values.py -v
```

## 6. Resultado esperado

El diccionario del conjunto de datos original de la UCI indica que no existen valores faltantes en ninguna de las 37 columnas.

Esta condición debe verificarse en el conjunto de datos extraído.

Si no se detectan valores faltantes, no se aplicará ninguna imputación.

El módulo permanece disponible para detectar valores faltantes en futuras versiones del conjunto de datos.