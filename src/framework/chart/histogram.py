from typing import List

import pandas as pd
from matplotlib import pyplot as plt

from src.framework.chart.chart import Chart


class Histogram(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)

    def plot(self) -> None:
        plt.hist(self.dataframe[self.columns[0]])
        plt.title(f"{self.title} {self.columns[0]}")
        plt.xlabel(self.columns[0])
        plt.ylabel('Frecuencia')
        plt.show()
