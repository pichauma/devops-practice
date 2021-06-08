from unittest.mock import patch
import numpy as np
import pandas as pd
from formation_devops.domain import clean, load


def test_clean_iris():
    iris = pd.DataFrame(
        [
            (np.nan, 1, 1, 1, 'test'),
            (1, np.nan, 1, 1, 'test'),
            (1, 1, np.nan, 1, 'test'),
            (1, 1, 1, np.nan, 'test'),
        ],
        columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'other'],
    )
    result = clean.clean_iris(iris)
    expected_result = pd.DataFrame(
        [
            (1.0, 1.0, 1.0, 1.0, 'test'),
            (1, 1, 1, 1, 'test'),
            (1, 1, 1, 1, 'test'),
            (1, 1, 1, 1, 'test'),
        ],
        columns=['SEPAL_LENGTH', 'SEPAL_WIDTH', 'PETAL_LENGTH', 'PETAL_WIDTH', 'OTHER'],
    )
    pd.testing.assert_frame_equal(result, expected_result)


@patch('formation_devops.domain.load.query_database')
def test_clean_data_from_database_with_unittest_patch(query_database):
    query_database.return_value = pd.DataFrame(
        [
            (1.0, 'other_value'),  # first row
            (np.NaN, 'other_value'),  # second row
            (2.0, 'other_value'),  # third row
        ],
        columns=['first_column', 'other_column'],
    )
    columns = ['first_column']
    result = clean.clean_data_from_database(columns)
    expected_result = pd.DataFrame(
        [
            (1.0, 'other_value'),  # first row
            (1.5, 'other_value'),  # second row
            (2.0, 'other_value'),  # third row
        ],
        columns=['first_column', 'other_column'],
    )
    pd.testing.assert_frame_equal(result, expected_result)


def mocked_query_database():
    data = pd.DataFrame(
        [
            (1.0, 'other_value'),  # first row
            (np.NaN, 'other_value'),  # second row
            (2.0, 'other_value'),  # third row
        ],
        columns=['first_column', 'other_column'],
    )
    return data


def test_clean_data_from_database_with_monkepatch(monkeypatch):
    columns = ['first_column']
    monkeypatch.setattr(load, "query_database", mocked_query_database)
    result = clean.clean_data_from_database(columns)
    expected_result = pd.DataFrame(
        [
            (1.0, 'other_value'),  # first row
            (1.5, 'other_value'),  # second row
            (2.0, 'other_value'),  # third row
        ],
        columns=['first_column', 'other_column'],
    )
    pd.testing.assert_frame_equal(result, expected_result)
