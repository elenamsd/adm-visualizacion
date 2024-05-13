from typing import List

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from src.framework.chart.chart import Chart


class ScatterPlot(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)

    def plot(self) -> None:
        if len(self.columns) < 2:
            raise ValueError("ScatterPlot necesita al menos 2 columnas")

        if len(self.columns) > 2:
            self._multigroup_plot()
        else:
            sns.scatterplot(data=self.dataframe, x=self.columns[0], y=self.columns[1])
            plt.title(f"{self.title} {self.columns[0]} and {self.columns[1]}")
            plt.show()

    def _multigroup_plot(self) -> None:
        figure, axis = plt.subplots(figsize=(10, 6))

        sns.scatterplot(data=self.dataframe, x=self.columns[0], y=self.columns[1], hue=self.columns[2])

        axis.set_xlabel(self.columns[0])
        axis.set_ylabel(self.columns[1])
        axis.set_title(f"{self.title} {self.columns[0]} and {self.columns[1]}")
        axis.legend()
        plt.show()