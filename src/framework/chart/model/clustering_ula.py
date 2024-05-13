from typing import List

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

from src.framework.chart.model.model import Model


class ClusteringULA(Model):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]):
        super().__init__(dataframe, title, columns)

    def algorithm(self):
        x = self.dataframe[self.columns]
        model = KMeans(n_clusters=2, random_state=42)
        model.fit(x)

        # Hacer predicciones
        y_pred = model.predict(x)
        self.dataframe['Cluster'] = model.labels_
        return x, y_pred

    def plot(self):
        x, y_pred = self.algorithm()
        plt.figure(figsize=(8, 6))
        self.dataframe.plot(kind='scatter', x='Feature1', y='Feature2', c='Cluster', cmap='viridis', colorbar=False)
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.title('Agrupamiento K-Means')
        plt.show()
