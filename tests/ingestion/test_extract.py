
import pandas as pd
import pytest

from src.ingestion.extract import extract_dataset


# ============================================================
# FIXTURES
# ============================================================

# @pytest.fixture: crea recursos reutilizables para las pruebas.
@pytest.fixture
def valid_csv(tmp_path):                    # tmp_path: crear directorios y archivos temporales.

    file_path = tmp_path / "students.csv"

    df = pd.DataFrame({
        "Age": [20, 25, 30],
        "Gender": ["Male", "Female", "Male"],
        "Target": ["Graduate", "Dropout", "Enrolled"]
    })

    df.to_csv(
        file_path,
        sep=";",
        index=False,
        encoding="utf-8"
    )

    return file_path


# ============================================================
# EXTRACTION TESTS
# ============================================================

def test_extract_dataset_successfully(valid_csv):

    result = extract_dataset(valid_csv)

    assert isinstance(result, pd.DataFrame)

    assert result.shape == (3, 3)

    assert list(result.columns) == [
        "Age",
        "Gender",
        "Target"
    ]


def test_extract_dataset_does_not_modify_source_file(valid_csv):

    original_content = valid_csv.read_bytes()       # .read_bytes(): Permite leer el contenido de un archivo como una secuencia de bytes.

    extract_dataset(valid_csv)

    modified_content = valid_csv.read_bytes()

    assert original_content == modified_content
    
    
def test_missing_file_raises_error(tmp_path):

    file_path = tmp_path / "nonexistent.csv"

    with pytest.raises(FileNotFoundError):

        extract_dataset(file_path)
        
        
# Esta prueba verifica que la función rechace archivos CSV que no contienen registros.
def test_empty_dataset_raises_error(tmp_path):

    file_path = tmp_path / "empty.csv"

    file_path.write_text(
        "Age;Gender;Target\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError):

        extract_dataset(file_path)
        
        
# Esta prueba verifica que nuestra función rechace archivos que contienen una sola columna.
def test_single_column_csv_raises_error(tmp_path):

    file_path = tmp_path / "single_column.csv"

    file_path.write_text(
        "Age\n20\n25\n30\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError):

        extract_dataset(file_path)
        

# Esta prueba verifica que nuestra función detecte un separador incorrecto.
def test_incorrect_separator_raises_error(valid_csv):

    with pytest.raises(ValueError):

        extract_dataset(
            valid_csv,
            sep=","
        )
        
# Esta prueba es muy importante cuando trabajamos con archivos CSV provenientes de diferentes fuentes.
def test_invalid_encoding_raises_error(tmp_path):

    file_path = tmp_path / "invalid_encoding.csv"

    file_path.write_bytes(                          # .write_bytes: Porque queremos introducir una secuencia de bytes que no sea válida como UTF-8.
        b"Age;Gender;Target\n20;Male;\xff\n"
    )

    with pytest.raises(ValueError, match="No se puede decodificar"):

        extract_dataset(file_path)
        

# Esta prueba comprueba que la función pueda trabajar con 
# rutas relativas utilizando la raíz del proyecto.
def test_relative_path_uses_project_root(tmp_path, monkeypatch):

    import src.ingestion.extract as extract_module

    project_root = tmp_path

    relative_path = "data/students.csv"

    file_path = project_root / relative_path

    # Obtiene el directorio padre de nuestro archivo.
    # y crea los archivos padre si no existen.
    file_path.parent.mkdir(parents=True)

    pd.DataFrame({
        "Age": [20],
        "Gender": ["Male"],
        "Target": ["Graduate"]
    }).to_csv(
        file_path,
        sep=";",
        index=False
    )

    # monkeypatch.setattr(): permite modificar temporalmente atributos,
    # variables de entorno y otros elementos durante una prueba.
    monkeypatch.setattr(
        extract_module,
        "PROJECT_ROOT",
        project_root
    )

    result = extract_dataset(relative_path)

    assert result.shape == (1, 3)
