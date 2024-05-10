from typing import List

import pandas as pd
from matplotlib import pyplot as plt

from src.framework.chart.chart import Chart


class LineChart(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)

    def plot(self) -> None:
        if len(self.columns) > 1:
            self._multigroup_plot()
        else:
            column_frequency: pd.DataFrame = self.dataframe[self.columns[0]].value_counts().sort_index()

            plt.plot(column_frequency.index, column_frequency.values)
            plt.xlabel(self.columns[0])
            plt.ylabel("Frequency")
            plt.title(f"{self.title} {self.columns[0]}")
            plt.show()

    def _multigroup_plot(self) -> None:
        grouped_dataframe = self.dataframe.groupby(self.columns[0])[self.columns[1]].value_counts()
        unique_x_values = sorted(self.dataframe[self.columns[0]].unique())
        unique_colors = sorted(self.dataframe[self.columns[1]].unique())

        figure, axis = plt.subplots(figsize=(10, 6))

        for index, x_value in enumerate(unique_x_values):
            color_frequencies = [grouped_dataframe.loc[x_value].get(color, 0) for color in unique_colors]
            axis.plot(unique_colors, color_frequencies, label=x_value)

        axis.set_xlabel(self.columns[1])
        axis.set_ylabel('Frequency')
        axis.set_title(f"{self.title} {self.columns[0]} and {self.columns[1]}")
        axis.legend(loc='upper left', bbox_to_anchor=(1, 1), title=self.columns[0])
        plt.show()
