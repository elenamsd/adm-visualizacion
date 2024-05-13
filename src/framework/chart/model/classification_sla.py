from typing import List

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import seaborn as sns

from src.framework.chart.model.model import Model


class ClassificationSLA(Model):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]):
        super().__init__(dataframe, title, columns)

    def algorithm(self):
        X = self.dataframe[self.columns]
        y = self.dataframe[self.columns[-1]]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LogisticRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Precisión de la clasificación:", accuracy)
        return y_test, y_pred

    def plot(self):
        y_test, y_pred = self.algorithm()
        plt.figure(figsize=(8, 6))
        sns.heatmap(pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']), annot=True, fmt='d')
        plt.title(f"Confusion Matrix - {self.title}")
        plt.show()
