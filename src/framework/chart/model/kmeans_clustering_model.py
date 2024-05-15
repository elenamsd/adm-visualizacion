from typing import List

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans, kmeans_plusplus

from src.framework.chart.model.model import Model


class KMeansClusteringModel(Model):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]):
        super().__init__(dataframe, title, columns)

    def algorithm(self):
        x = self.dataframe[self.columns].values

        model = KMeans(n_clusters=2, init="k-means++", random_state=42)
        model.fit(x)
        y_pred = model.predict(x)

        self.dataframe['Cluster'] = model.labels_
        return x, y_pred, model.cluster_centers_

    def plot(self):
        x, y_pred, centers_init = self.algorithm()
        self.dataframe.plot(kind='scatter', x=self.columns[0], y=self.columns[1], c='Cluster', cmap='viridis', colorbar=False)
        plt.scatter(centers_init[:, 0], centers_init[:, 1], c="b", s=50)
        plt.xlabel(self.columns[0])
        plt.ylabel(self.columns[1])
        plt.title('Agrupamiento K-Means')
        plt.show()
