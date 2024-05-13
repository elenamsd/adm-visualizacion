from typing import List

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from src.framework.chart.model.model import Model


class RegressionA(Model):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]):
        super().__init__(dataframe, title, columns)

    def algorithm(self):
        x = self.dataframe[self.columns]
        y = self.dataframe[self.columns[-1]]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        mse = mean_squared_error(y_test, y_pred)
        print("Error cuadrático medio de la regresión:", mse)
        return y_test, y_pred

    def plot(self):
        y_test, y_pred = self.algorithm()
        plt.figure(figsize=(8, 6))
        plt.plot(y_test, label='Valores reales')
        plt.plot(y_pred, label='Predicciones', linestyle='--')
        plt.xlabel('Índice de la muestra')
        plt.ylabel('Valor de la diabetes')
        plt.title('Regresión SVR en conjunto de datos Diabetes')
        plt.legend()
        plt.show()
