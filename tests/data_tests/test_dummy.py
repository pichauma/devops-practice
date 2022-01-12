import os
import tempfile

import pytest


def test_dumm():
    assert True


@pytest.fixture()
def cleandir():
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)


@pytest.mark.usefixtures("cleandir")
def test():
    print("use fixtures")
    assert True


