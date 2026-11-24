# Diccionario de datos

## Descripción general

Este directorio contiene el diccionario de datos para el conjunto de datos **Predicción de la deserción y el éxito académico de los estudiantes**.

El diccionario de datos ofrece una descripción estructurada de las variables del conjunto de datos, incluyendo sus definiciones, tipos de datos, clasificaciones analíticas, dominios y etapas de disponibilidad.

Su propósito es establecer una comprensión coherente de los datos antes de proceder con la validación, transformación, análisis exploratorio y modelado predictivo.

## Información del conjunto de datos

| Atributo | Descripción |
|---|---|
| Conjunto de datos | Predicción de la deserción y el éxito académico de los estudiantes |
| Fuente | Repositorio de Aprendizaje Automático de la UCI (UCI Machine Learning Repository) |
| ID del conjunto de datos | 697 |
| Observaciones | 4.424 |
| Variables predictoras | 36 |
| Variable objetivo | 1 |
| Total de variables | 37 |
| Tipo de problema | Clasificación multiclase |

## Descripción de los archivos

| Archivo | Descripción |
|---|---|
| `data_dictionary.csv` | Documentación estructurada de todas las variables del conjunto de datos. |

## Estructura del diccionario de datos

El archivo CSV contiene los siguientes metadatos:

| Columna | Descripción |
|---|---|
| `column_name` | Nombre original de la variable en el conjunto de datos. |
| `description` | Explicación del significado de la variable. |
| `data_type` | Tipo de dato detectado en el conjunto de datos original mediante `pandas`. |
| `variable_type` | Clasificación analítica (por ejemplo: categórica, binaria, ordinal, continua, de conteo u objetivo). |
| `data_group` | Agrupación funcional de la variable (por ejemplo: demográfica, académica, financiera o socioeconómica). |
| `domain` | Descripción de las categorías, códigos, rangos o unidades de medida válidos. |
| `availability_stage` | Etapa en la que se espera que la información esté disponible. |
| `prediction_scenario` | Escenario de predicción en el que se puede considerar la variable. |
| `is_target` | Indicador booleano que identifica la variable objetivo. |
| `missing_count` | Número de valores faltantes detectados en la variable. |
| `unique_values` | Número de valores distintos observados en la variable. | |

## Disponibilidad de variables y escenarios de predicción

Las variables se clasifican según su disponibilidad esperada a lo largo del ciclo de vida del estudiante.

| Escenario | Descripción |
|---|---|
| `enrollment` | Información disponible en el momento de la inscripción del estudiante. |
| `first_semester` | Información sobre el rendimiento académico disponible tras el primer semestre. |
| `second_semester` | Información sobre el rendimiento académico disponible tras el segundo semestre. |
| `outcome` | Resultado final del estudiante, utilizado como objetivo de predicción. |

Esta clasificación facilita el desarrollo de distintos escenarios de predicción y ayuda a prevenir la fuga de información temporal (*temporal data leakage*).

Las variables registradas después de la inscripción no deben incluirse en un modelo destinado a predecir los resultados de los estudiantes en el momento de su inscripción.

Asimismo, antes de realizar el modelado, es necesario verificar la disponibilidad real y los periodos de referencia de determinadas variables contextuales.

## Proceso de generación

El diccionario de datos se genera de forma programática mediante Python.

El proceso de generación combina:

1. Metadatos de las variables definidos manualmente.
2. Tipos de datos detectados automáticamente.
3. Recuento de valores faltantes.
4. Recuento de valores únicos.
5. Clasificaciones según la etapa de predicción.

Para regenerar el diccionario, ejecute el siguiente comando desde la raíz del proyecto:

```bash
python -m src.documentation.create_data_dictionary
```

El archivo generado se guarda en:

```text
docs/data_dictionary/data_dictionary.csv
```

## Fuente de datos y atribución

Realinho, V., Vieira Martins, M., Machado, J., & Baptista, L. (2021).

*Predict Students' Dropout and Academic Success*.

UCI Machine Learning Repository.

https://doi.org/10.24432/C5MC89

Licencia del conjunto de datos: **Creative Commons Attribution 4.0 International (CC BY 4.0)**.