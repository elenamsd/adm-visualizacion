from typing import List

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier

from src.framework.chart.model.model import Model


class DecisionTreeClassifierModel(Model):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]):
        super().__init__(dataframe, title, columns)

    def algorithm(self):
        X = self.dataframe.select_dtypes(include=['number']).drop(self.columns[0], axis=1)
        y = self.dataframe[self.columns[0]]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = DecisionTreeClassifier(random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        print(f'Accuracy: {accuracy * 100:.2f}%')
        return y_test, y_pred

    def plot(self):
        if len(self.columns) != 1:
            raise ValueError('Se esperaba una sola columna para la variable objetivo')

        y_test, y_pred = self.algorithm()
        plt.figure(figsize=(8, 6))
        sns.heatmap(pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']), annot=True, fmt='d')
        plt.title(f"Confusion Matrix - {self.title}")
        plt.show()
