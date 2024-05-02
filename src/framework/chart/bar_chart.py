from typing import List

import pandas as pd
from matplotlib import pyplot as plt

from src.framework.chart.chart import Chart


class BarChart(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)

    def plot(self) -> None:
        column_frequency: pd.DataFrame = self.dataframe[self.columns[0]].value_counts()
        column_frequency.plot.bar(rot=0)
        plt.xlabel("Frequency")
        plt.ylabel(self.columns[0])
        plt.title(self.title)
        plt.show()





