# Ingesta de datos

## Descripción general

La capa de ingesta se encarga de extraer el conjunto de datos original de los estudiantes y estandarizar los nombres de sus columnas antes de pasar la información a las siguientes etapas del flujo de procesamiento (pipeline).

Esta capa establece una estructura de entrada coherente para el proyecto, sin realizar tareas de limpieza de datos, tratamiento de valores faltantes, ingeniería de características o transformaciones estadísticas.

## Módulos

### 1. `extract.py`

**Función:** `extract_dataset()`

Extrae el conjunto de datos original desde un archivo CSV y lo devuelve como un DataFrame de Pandas.

**Responsabilidades principales:**

- Determinar la ruta del archivo de datos.
- Verificar que el archivo de origen exista.
- Leer el archivo CSV utilizando el delimitador y la codificación configurados.
- Gestionar errores de decodificación y análisis (parsing) del archivo.
- Verificar que el conjunto de datos extraído no esté vacío.
- Comprobar que el archivo CSV contenga más de una columna.
- Delegar la normalización de los nombres de las columnas a `normalize_column_names()`.

**Parámetros:**

| Parámetro | Descripción | Valor predeterminado |
|---|---|---|
| `file_path` | Ubicación del archivo CSV de origen | `RAW_DATA_FILE` |
| `sep` | Delimitador del archivo CSV | `;` |
| `encoding` | Codificación del archivo | `utf-8` |

**Retorno:**

Un DataFrame de Pandas que contiene el conjunto de datos extraído con los nombres de las columnas estandarizados.

**Excepciones:**

- `FileNotFoundError`: El archivo de origen no existe.
- `ValueError`: Errores en la decodificación, el análisis o la estructura del conjunto de datos.

### 2. `normalize_columns.py`

**Función:** `normalize_column_names(df)`

Estandariza los nombres de las columnas de un DataFrame para garantizar la coherencia en todo el flujo de procesamiento analítico.

**Transformaciones:**

- Elimina los espacios en blanco al inicio y al final.
- Elimina las tabulaciones al inicio y al final.
- Convierte los nombres de las columnas a minúsculas.
- Preserva el DataFrame original sin modificarlo.
- Detecta nombres de columnas duplicados que puedan surgir durante el proceso de normalización.

**Parámetros:**

| Parámetro | Descripción |
|---|---|
| `df` | DataFrame de Pandas cuyos nombres de columna se van a estandarizar |

**Retorno:**

Una copia del DataFrame original con los nombres de las columnas normalizados. **Excepciones:**

- `TypeError`: El dato de entrada no es un DataFrame de Pandas.
- `ValueError`: La normalización genera nombres de columna duplicados.

## Flujo de datos

El proceso de ingesta sigue esta secuencia:

1. `extract_dataset()` recibe la ruta del archivo CSV de origen.
2. La función verifica que el archivo de origen exista.
3. Pandas lee el archivo CSV y lo convierte en un DataFrame.
4. `normalize_column_names()` estandariza los nombres de las columnas.
5. El DataFrame extraído se devuelve al flujo de procesamiento (*pipeline*).

```text
CSV original
| 
v
extract_dataset()
| 
v
Extracción del CSV
| 
v
normalize_column_names()
| 
v
DataFrame normalizado
| 
v
Siguiente etapa del flujo de procesamiento
```

## Decisiones de diseño

- **Separación de responsabilidades:** La extracción y la normalización de los nombres de columna se implementan como funciones independientes.
- **Operaciones no destructivas:** La normalización de los nombres de columna devuelve una copia del DataFrame de entrada.
- **Convención de nomenclatura coherente:** Los nombres de las columnas se estandarizan utilizando caracteres en minúsculas y eliminando espacios en blanco adicionales.
- **Gestión de errores:** Se manejan explícitamente las rutas no válidas, los problemas de codificación, los errores de análisis (*parsing*) y la presencia de nombres de columna duplicados.
- **Ausencia de transformaciones analíticas:** La capa de ingesta no modifica los valores de las variables, no imputa valores faltantes, no elimina observaciones ni genera nuevas variables (*feature engineering*).

## Alcance y limitaciones

La capa de ingesta se centra exclusivamente en la extracción de datos y la estandarización de los nombres de las columnas.

Las siguientes operaciones corresponden a etapas posteriores del flujo de procesamiento:

- Validación de datos.
- Limpieza de datos.
- Análisis y tratamiento de valores faltantes.
- Clasificación del tipo de variables.
- Ingeniería de variables (*feature engineering*).
- Preprocesamiento para modelos predictivos.

## Ejemplo de uso

```python
from src.ingestion.extract import extract_dataset

df = extract_dataset()

print(df.head())
print(df.columns.tolist())
```

El DataFrame resultante está listo para ser utilizado en las etapas de validación y preprocesamiento.