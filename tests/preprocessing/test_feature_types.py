import pandas as pd
import pytest

from src.preprocessing.feature_types import classify_feature_types
from src.ingestion.normalize_columns import normalize_column_names



def create_test_dataset():

    return pd.DataFrame({
        "Marital status": [1, 2],
        "Application order": [1, 2],
        "Gender": [1, 0],
        "Age at enrollment": [20, 25],
        "Admission grade": [150.5, 160.0],
        "Target": ["Graduate", "Dropout"]
    })


def create_test_dictionary():

    return pd.DataFrame({
        "column_name": [
            "Marital status",       # categorical
            "Application order",    # ordinal
            "Gender",               # categorical
            "Age at enrollment",    # numerical
            "Admission grade",      # numerical
            "Target"                # target
        ],
        "variable_type": [
            "categorical",
            "ordinal",
            "binary",
            "integer",
            "continuous",
            "target"
        ]
    })


def test_categorical_classification():

    df = create_test_dataset()
    dictionary = create_test_dictionary()

    groups = classify_feature_types(df, dictionary)

    assert groups["categorical"] == [
        "marital status",
        "gender"
    ]


def test_ordinal_classification():
    
    df = create_test_dataset()
    dictionary = create_test_dictionary()
    
    groups = classify_feature_types(df, dictionary)
    
    assert groups["ordinal"] == ["application order"]
    
    
def test_numerical_classification():
    
    df = create_test_dataset()
    dictionary = create_test_dictionary()
    
    groups = classify_feature_types(df, dictionary)
    
    assert groups["numerical"] == [
        "age at enrollment", 
        "admission grade"
    ]
    
def test_target_classification():
    
    df = create_test_dataset()
    dictionary = create_test_dictionary()
    
    groups = classify_feature_types(df, dictionary)
    
    assert groups["target"] == ["target"]
    

def test_all_columns_are_classified():

    df = create_test_dataset()
    dictionary = create_test_dictionary()

    groups = classify_feature_types(df, dictionary)

    classified_columns = [
        column
        for columns in groups.values()
        for column in columns
    ]
    
    # normalizar las columnas del df
    normalize_columns = normalize_column_names(df).columns

    assert len(classified_columns) == len(df.columns)
    assert set(classified_columns) == set(normalize_columns)
    
    
def test_missing_dictionary_columns_raise_error():

    df = create_test_dataset()

    dictionary = pd.DataFrame({
        "column_name": ["Age at enrollment"],
        "variable_type": ["integer"]
    })

    with pytest.raises(ValueError):

        classify_feature_types(df, dictionary)


def test_unknown_variable_type_raises_error():

    df = pd.DataFrame({
        "Age": [20]
    })

    dictionary = pd.DataFrame({
        "column_name": ["Age"],
        "variable_type": ["unknown"]
    })

    with pytest.raises(ValueError):

        classify_feature_types(df, dictionary)
        
     
        
def test_non_dataframe_input_raises_error():

    with pytest.raises(TypeError):

        classify_feature_types(
            ["Graduate"],
            create_test_dictionary()
        )