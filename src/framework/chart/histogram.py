from typing import List

import pandas as pd
from matplotlib import pyplot as plt

from src.framework.chart.chart import Chart


class Histogram(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)

    def plot(self) -> None:
        plt.hist(self.dataframe[self.columns[0]])
        plt.title(self.title)
        plt.xlabel('Frecuencia')
        plt.ylabel(self.columns[0])
        plt.show()
