import numpy as np
import pandas as pd
from formation_devops.domain import clean, load
def test_clean_iris():
    iris = pd.DataFrame([
        (np.nan, 1, 1, 1, 'test'),
        (1, np.nan, 1, 1, 'test'),
        (1, 1, np.nan, 1, 'test'),
        (1, 1, 1, np.nan, 'test'),
    ], columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'other'])
    result = clean.clean_iris(iris)
    expected_result = pd.DataFrame([
        (1.0, 1.0, 1.0, 1.0, 'test'),
        (1, 1, 1, 1, 'test'),
        (1, 1, 1, 1, 'test'),
        (1, 1, 1, 1, 'test'),
    ], columns=['SEPAL_LENGTH', 'SEPAL_WIDTH', 'PETAL_LENGTH', 'PETAL_WIDTH', 'OTHER'])
    pd.testing.assert_frame_equal(result, expected_result)
