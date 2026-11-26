
import pandas as pd
import pytest

from src.ingestion.normalize_columns import normalize_column_names


# ============================================================
# FIXTURES
# ============================================================

@pytest.fixture                                                 # Indica que es un recurso que puede proporcionar a las pruebas que lo necesiten
def sample_dataframe():

    return pd.DataFrame({
        " Age ": [20, 25, 30],
        " Gender\t": ["Male", "Female", "Male"],
        "Target ": ["Graduate", "Dropout", "Enrolled"]
    })


# ============================================================
# NORMALIZATION TESTS
# ============================================================

def test_normalize_column_names_correctly(sample_dataframe):

    result = normalize_column_names(sample_dataframe)

    expected_columns = [
        "age",
        "gender",
        "target"
    ]

    assert list(result.columns) == expected_columns


def test_normalization_does_not_modify_original_dataframe(sample_dataframe):

    original_df = sample_dataframe.copy(deep=True)

    normalize_column_names(sample_dataframe)

    pd.testing.assert_frame_equal(  # comprueba si el primer dataframe es igual al segundo
        sample_dataframe,
        original_df
    )


def test_normalization_returns_dataframe(sample_dataframe):

    result = normalize_column_names(sample_dataframe)

    assert isinstance(result, pd.DataFrame)


def test_normalization_returns_independent_copy(sample_dataframe):

    result = normalize_column_names(sample_dataframe)

    assert result is not sample_dataframe
    

def test_non_dataframe_input_raises_error():

    with pytest.raises(TypeError):                  # la función admite solo DataFrame
                                                    # al introducir una lista
        normalize_column_names(["Age", "Gender"])   # devuelve error


def test_duplicate_columns_after_normalization_raise_error():

    df = pd.DataFrame(
        [[20, 25]],
        columns=[" Age ", "age"]
    )

    with pytest.raises(ValueError):

        normalize_column_names(df)
        

def test_non_string_column_names_are_preserved():

    df = pd.DataFrame(
        [[20, "Graduate"]],
        columns=[0, " Target "]
    )

    result = normalize_column_names(df)

    assert list(result.columns) == [0, "target"]