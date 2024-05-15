from typing import List

import numpy as np
import pandas as pd
from sklearn import datasets
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from src.framework.chart.model.model import Model


class LinearRegressionModel(Model):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]):
        super().__init__(dataframe, title, columns)

    def algorithm(self):
        X = self.dataframe.select_dtypes(include=['number']).drop(self.columns[0], axis=1)
        y = self.dataframe[self.columns[0]]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        print(f'Error cuadrático medio de la regresión: {mse * 100:.2f}%')
        return X_test, y_test, y_pred

    def plot(self):
        X_test, y_test, y_pred = self.algorithm()
        X_test_sorted = X_test.iloc[:, 0].sort_values().values.reshape(-1, 1)
        y_pred_sorted = y_pred[np.argsort(X_test.iloc[:, 0])]

        plt.figure(figsize=(8, 6))
        plt.scatter(X_test_sorted, y_test, color='blue', label='Actual')
        plt.plot(X_test_sorted, y_pred_sorted, color='red', label='Predicted')
        # plt.plot(X_test.iloc[:, 0], y_pred, color='red', label='Predicted')
        plt.title('Actual vs Predicted')
        plt.xlabel('X')
        plt.ylabel('y')
        plt.legend()
        plt.show()
