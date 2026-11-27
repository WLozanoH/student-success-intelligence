# Student Success Intelligence

### Clasificación del resultado académico y análisis de factores asociados a la deserción universitaria

## 1. Descripción del proyecto

La deserción universitaria representa uno de los principales desafíos para las instituciones de educación superior, debido a sus implicancias académicas, económicas y sociales.

**Student Success Intelligence** es un proyecto de analítica de datos y aprendizaje automático (*Machine Learning*) orientado a estudiar los factores asociados al resultado académico de los estudiantes y desarrollar un modelo de clasificación multiclase que permita identificar patrones relacionados con la deserción, la continuidad y la culminación de los estudios universitarios.

La primera versión desarrolla un flujo reproducible de procesamiento, análisis, preparación y modelado de datos, utilizando información demográfica, socioeconómica, académica y macroeconómica.

El proyecto busca generar información analítica que contribuya a comprender los resultados académicos y respaldar la toma de decisiones en instituciones de educación superior.

## 2. Objetivos del proyecto

- Analizar los factores demográficos, socioeconómicos y académicos asociados al resultado de los estudiantes.
- Identificar patrones relacionados con la deserción, continuidad y culminación de los estudios.
- Construir un flujo reproducible de extracción, transformación y preparación de datos.
- Desarrollar un modelo de clasificación multiclase para estimar los resultados académicos.
- Evaluar el rendimiento predictivo mediante métricas de clasificación.
- Interpretar los resultados e identificar las características relevantes para el modelo.
- Desarrollar visualizaciones y paneles analíticos para facilitar la interpretación de los resultados.

## 3. Fuente de datos

**Conjunto de datos:** Predict Students' Dropout and Academic Success.

**Fuente original:** UCI Machine Learning Repository.

**Fuente complementaria:** Kaggle - Predictors of Student Retention in Higher Education.

**Características del conjunto de datos:**

- 4,424 registros de estudiantes.
- 36 variables predictoras.
- 1 variable objetivo: `Target`.
- Tres categorías de clasificación:
  - `Dropout`: estudiante que abandonó sus estudios.
  - `Enrolled`: estudiante que continúa matriculado.
  - `Graduate`: estudiante que culminó sus estudios.

**Variable objetivo:**

`Target`

La variable representa el resultado académico del estudiante y constituye la variable que el modelo intentará clasificar.

**Referencia académica:**

Realinho, V., Vieira Martins, M., Machado, J., & Baptista, L. (2021). Predict Students' Dropout and Academic Success. UCI Machine Learning Repository.

https://doi.org/10.24432/C5MC89

**Licencia:** CC BY 4.0.

## 4. Alcance predictivo de V1

La primera versión del proyecto contempla un único experimento de clasificación multiclase.

**Objetivo predictivo:**

Clasificar el resultado académico de los estudiantes (`Graduate`, `Dropout` o `Enrolled`) utilizando las características disponibles hasta el segundo semestre académico.

**Información utilizada:**

- Características demográficas.
- Información de admisión.
- Información financiera.
- Antecedentes académicos.
- Indicadores académicos del primer semestre.
- Indicadores académicos del segundo semestre.
- Variables macroeconómicas.

El análisis académico contempla indicadores individuales por semestre y características acumuladas, con el propósito de estudiar el rendimiento y su relación con el resultado final.

**Consideración metodológica:**

Este modelo no se presenta como un sistema de alerta temprana. Su propósito en V1 es clasificar los resultados académicos utilizando la información considerada hasta el segundo semestre.

La disponibilidad temporal de las características y su relación con la variable objetivo serán verificadas antes del entrenamiento para evitar filtraciones de información (*data leakage*).

## 5. Stack tecnológico

| Tecnología | Propósito |
|---|---|
| Python | Procesamiento de datos y Machine Learning |
| Pandas / NumPy | Manipulación y análisis de datos |
| Scikit-learn | Preprocesamiento y modelado predictivo |
| Pytest | Pruebas automatizadas |
| SQL Server | Gestión y almacenamiento de datos analíticos |
| SQL | Consultas y transformación de datos |
| Power BI | Visualización e inteligencia de negocios |
| PBIP | Desarrollo de proyectos de Power BI con control de versiones |
| Git / GitHub | Control de versiones y documentación |

## 6. Metodología y arquitectura

El proyecto toma como referencia la metodología CRISP-DM y una arquitectura de procesamiento de datos por capas.

**Flujo general propuesto:**

```text
Datos originales
      |
      v
Extracción y normalización
      |
      v
Validación de datos
      |
      v
Preparación y limpieza
      |
      v
Feature Engineering
      |
      v
Dataset predictivo
      |
      v
Preprocesamiento
      |
      v
Modelado y evaluación
      |
      v
Interpretación de resultados
      |
      v
Visualización y reporting
```

El código se desarrolla mediante módulos reutilizables, con pruebas automatizadas y documentación técnica para facilitar la reproducibilidad y el mantenimiento.

## 7. Estructura del proyecto

```text
Student-Success-Intelligence/
│
├── config/
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│
├── src/
│   ├── config/
│   ├── ingestion/
│   ├── validation/
│   ├── preprocessing/
│   └── feature_engineering/
│
├── sql/
├── orchestration/
├── tests/
├── docs/
│
├── powerbi/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 8. Roadmap y estado del proyecto

**V1 — Student Success Intelligence**

| Hito | Descripción | Estado |
|---|---|---|
| H1 | Configuración del proyecto y repositorio | Completado |
| H2 | Comprensión y análisis exploratorio de datos | Completado |
| H3 | Validación de datos | Completado |
| H4 | Preparación de datos y Feature Engineering | En progreso |
| H5 | Modelado predictivo y evaluación | Pendiente |
| H6 | Análisis de resultados y reporting | Pendiente |

**H4 — Data Preparation & Feature Engineering**

- Data Cleaning.
- Missing Value Analysis.
- Feature Type Classification.
- Academic Features Analysis.
- Feature Engineering.
- Predictive Dataset Definition.
- Preprocessing Pipeline.

**H5 — Predictive Modeling**

- Dummy Classifier.
- Logistic Regression.
- Random Forest.
- Model Evaluation.
- Model Interpretation.

**H6 — Analytics & Reporting**

- Results Analysis.
- Data Visualizations.
- Business Recommendations.
- Final Documentation.

## 9. Evolución futura

Una vez completada y evaluada V1, el proyecto podrá evolucionar hacia un sistema de inteligencia académica con funcionalidades adicionales:

- Modelos de alerta temprana (*Early Warning*).
- Predicción basada en información disponible al momento de la matrícula.
- Evaluación del progreso académico al finalizar el primer semestre.
- Comparación de modelos según el momento de predicción.
- Monitoreo del riesgo académico.
- Dashboards orientados a la gestión universitaria.

Estas funcionalidades se consideran posibles extensiones futuras y no forman parte del alcance predictivo de V1.

## 10. Aviso legal

Este proyecto utiliza un conjunto de datos educativos públicos correspondiente a una institución de educación superior portuguesa.

Su desarrollo tiene fines educativos, analíticos y demostrativos, como parte de un proyecto de portafolio profesional.

Los resultados de los modelos representan estimaciones estadísticas y no deben utilizarse como juicios definitivos sobre estudiantes individuales ni como único criterio para tomar decisiones académicas.