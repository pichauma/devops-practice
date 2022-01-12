import pandas as pd

from formation_devops.domain import clean, load
from formation_devops.domain.regression import LinearIris
from formation_devops.infrastructure.files import FileManager
from formation_devops.settings import DATA_DIR  # type: ignore

files = FileManager(DATA_DIR)

def test_train_model():
    # TODO: Add a test to assert the accuracy of the model is over 80%
    #Accuracy calculation formula : accuracy = 100-abs((real_value-predicted_value)/real_value*100)
    # Where real_value = real value of the object
    #       predicted_value = value predicted by the model
    ...