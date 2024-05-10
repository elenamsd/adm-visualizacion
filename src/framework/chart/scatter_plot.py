from typing import List

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from src.framework.chart.chart import Chart


class ScatterPlot(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)

    def plot(self) -> None:
        # dataframe = self.dataframe.groupby([self.columns[0], self.columns[1]]).size().reset_index(name='Frequency')
        # plt.figure(figsize=(10, 8))
        sns.scatterplot(data=self.dataframe, x=self.columns[0], y=self.columns[1])
        plt.title(f"{self.title} {self.columns[0]} and {self.columns[1]}")
        plt.show()
