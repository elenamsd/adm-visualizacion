from typing import List, Any

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

from src.framework.chart.model.model import Model


class KMeansClusteringModel(Model):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]):
        super().__init__(dataframe, title, columns)

    def algorithm(self):
        n_clusters: int = self.dataframe.columns.get_loc(self.columns[0]) + 1
        x = self.dataframe[self.columns[1:]].values

        model = KMeans(n_clusters=n_clusters, init="k-means++", random_state=42)
        model.fit(x)
        y_pred = model.predict(x)

        self.dataframe['Cluster'] = model.labels_
        return x, y_pred, model.cluster_centers_

    def plot(self):
        x, y_pred, centers_init = self.algorithm()
        self.dataframe.plot(kind='scatter', x=self.columns[1], y=self.columns[2], c='Cluster', cmap='viridis', colorbar=False)
        plt.scatter(centers_init[:, 0], centers_init[:, 1], c="b", s=50)
        plt.xlabel(self.columns[1])
        plt.ylabel(self.columns[2])
        plt.title('Agrupamiento K-Means')
        plt.show()
