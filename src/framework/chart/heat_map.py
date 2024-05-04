from typing import List

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from src.framework.chart.chart import Chart


class HeatMap(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)


    def plot(self) -> None:
        sns.heatmap(self.dataframe.groupby([self.columns[0], self.columns[1]]).size().unstack().T, cmap='viridis')
        plt.title(self.title)
        plt.xlabel(self.columns[0])
        plt.ylabel(self.columns[1])
        plt.show()



    # correlogramas, boxplots, curvas de densidad, diagramas de violín