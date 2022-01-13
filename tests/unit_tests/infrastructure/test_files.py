

import os

import pandas as pd

from formation_devops.infrastructure.files import FileManager

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
DATA_DIR = os.path.join(REPO_DIR, 'data')


class Test_files:
    files = FileManager(DATA_DIR)

    def test_load(self):
        df_expected = pd.DataFrame(
            {
                'sepal_length': {0: '5.1', 1: '4.9'},
                'sepal_width': {0: '3.5', 1: '3'},
                'petal_length': {0: '1.4', 1: '1.4'},
                'petal_width': {0: '0.2', 1: '0.2'},
                'species': {0: 'setosa', 1: 'setosa'},
            }
        )
        df = self.files.load('raw/iris.csv', nrows=2, dtype='str')

        assert df.equals(df_expected)
