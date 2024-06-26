from typing import List

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from src.framework.chart.chart import Chart


class BarChart(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)

    def plot(self) -> None:
        if len(self.columns) > 1:
            self._multigroup_plot()
        else:
            column_frequency: pd.DataFrame = self.dataframe[self.columns[0]].value_counts()
            column_frequency.plot.bar(rot=0)

            plt.xlabel(self.columns[0])
            plt.ylabel("Frequency")
            plt.title(f"{self.title} {self.columns[0]}")
            plt.show()

    def _multigroup_plot(self) -> None:
        grouped_dataframe: pd.DataFrame = self.dataframe.groupby(self.columns[0])[self.columns[1]].value_counts()
        unique_x_values: List[str] = sorted(self.dataframe[self.columns[0]].unique())
        unique_colors: List[str] = sorted(self.dataframe[self.columns[1]].unique())

        bar_positions: np.ndarray = np.arange(len(unique_colors))
        bar_width: float = 0.15

        figure, axis = plt.subplots(figsize=(10, 6))

        for index, x_value in enumerate(unique_x_values):
            color_frequencies: List[int] = [grouped_dataframe.loc[x_value].get(color, 0) for color in unique_colors]
            bars: int = axis.bar(bar_positions + bar_width * index, color_frequencies, bar_width, label=x_value)
            axis.bar_label(bars, padding=3)

        axis.set_xlabel(self.columns[1])
        axis.set_ylabel('Frequency')
        axis.set_title(f"{self.title} {self.columns[0]} and {self.columns[1]}")
        axis.set_xticks(bar_positions + bar_width * (len(unique_x_values) - 1) / 2)
        axis.set_xticklabels(unique_colors)
        axis.legend(loc='upper left', bbox_to_anchor=(1, 1), title=self.columns[0])
        plt.show()
