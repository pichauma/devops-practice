# Import Standard Libraries
import pandas as pd
import numpy as np

# Import ML Libaries
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


def converter(specie):
    if specie == 'setosa':
        return 0
    elif specie == 'versicolor':
        return 1
    else:
        return 2


class LinearIris:
    def __init__(self, iris_df):
        self.iris_df = iris_df
        self.y_train = None
        self.X_train = None
        self.y_test = None
        self.X_test = None

        # Instantiating LinearRegression() Model
        self.lr = LinearRegression()

    def prepare_df(self):
        # Converting Objects to Numerical dtype
        # TODO: prepare_df function applies the converter to the SPECIES column in the iris dataframe
        ...

    def split_model(self, iris_df):
        # Variables
        X = iris_df.drop(labels='SEPAL_LENGTH', axis=1)
        y = iris_df['SEPAL_LENGTH']

        # Splitting the Dataset
        # TODO: Set the values self.X_train, self.X_test, self.y_train, self.y_test using the train_test_split function
        self.X_train, self.X_test, self.y_train, self.y_test = ...

    def train_model(self):
        # TODO: Train/Fit the Model with the self.X_train, self.y_train variables

        # TODO: Make a Prediction with X_test dataframe and fill a variable named pred with it
        pred = ...

        # Evaluating Model's Performance
        print('Mean Absolute Error:', mean_absolute_error(self.y_test, pred))
        print('Mean Squared Error:', mean_squared_error(self.y_test, pred))
        print('Mean Root Squared Error:', np.sqrt(mean_squared_error(self.y_test, pred)))

    def predict(self, df):
        pred = self.lr.predict(df)
        return pred
