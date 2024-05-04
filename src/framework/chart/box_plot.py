from typing import List

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from src.framework.chart.chart import Chart


class BoxPlot(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)


    def plot(self) -> None:
        sns.boxplot(x=self.columns[0], y=self.columns[1], data=self.dataframe)
        plt.title(self.title)
        plt.show()