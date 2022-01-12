import os

import pandas as pd

from formation_devops.infrastructure.files import FileManager

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
DATA_DIR = os.path.join(REPO_DIR, 'data')


class Test_files:
    files = FileManager(DATA_DIR)

    def test_load(self):
        """

        Returns
        -------

        """
        # Given

        # When
        df_tested = self.files.load('raw/iris.csv', nrows=2, dtype='str')
        assert df_tested.equals(df_expected)
        # TODO
