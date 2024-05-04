from typing import List

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from src.framework.chart.chart import Chart

# TODO: PETA CON VARIABLES CATEGÓRICAS
class ProbabilityDensityFunction(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)


    def plot(self) -> None:
        sns.kdeplot(data=self.dataframe[self.columns[0]], fill=True, color='r')
        plt.title(self.title)
        plt.xlabel('Density')
        plt.xlabel('Number of Casualties')
        plt.show()


    # correlogramas