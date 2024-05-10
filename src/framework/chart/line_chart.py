from typing import List

import pandas as pd
from matplotlib import pyplot as plt

from src.framework.chart.chart import Chart


class LineChart(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)

    def plot(self) -> None:
        column_frequency: pd.DataFrame = self.dataframe[self.columns[0]].value_counts().sort_index()

        plt.plot(column_frequency.index, column_frequency.values)
        plt.xlabel(self.columns[0])
        plt.ylabel("Frequency")
        plt.title(f"{self.title} {self.columns[0]}")
        plt.show()
