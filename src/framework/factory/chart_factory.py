from typing import List

import pandas as pd

from src.framework.enum.chart_type import ChartType


class ChartFactory:

    @staticmethod
    def create_chart(chart_type: ChartType, dataframe: pd.DataFrame, columns: List[str]) -> None:
        if chart_type.is_bar_chart():
            return ChartFactory._create_bar_chart(chart_type, dataframe, columns)
        elif chart_type.is_line_chart():
            return ChartFactory._create_bar_chart(chart_type, dataframe, columns)
        elif chart_type.is_histogram():
            return ChartFactory._create_bar_chart(chart_type, dataframe, columns)
        elif chart_type.is_scatter_plot():
            return ChartFactory._create_bar_chart(chart_type, dataframe, columns)
        elif chart_type.is_heat_map():
            return ChartFactory._create_bar_chart(chart_type, dataframe, columns)
        elif chart_type.is_box_plot():
            return ChartFactory._create_bar_chart(chart_type, dataframe, columns)
        elif chart_type.is_violin_plot():
            return ChartFactory._create_bar_chart(chart_type, dataframe, columns)
        elif chart_type.is_probability_density_function():
            return ChartFactory._create_bar_chart(chart_type, dataframe, columns)
        elif chart_type.is_pair_plot():
            return ChartFactory._create_bar_chart(chart_type, dataframe, columns)
        else:
            raise ValueError('Invalid chart type')


    # @classmethod
    # def (cls, dataframe: pd.DataFrame) -> List[str]:
    #     pass


    @classmethod
    def _create_bar_chart(cls, chart_type: ChartType, dataframe: pd.DataFrame, columns: List[str]) -> None:
        # if len(columns) != 1:
        #     raise ValueError(f"{chart_type.name} only supports one column")
        ChartFactory._create_chart(chart_type, dataframe, columns)


    @classmethod
    def _create_chart(cls, chart_type: ChartType, dataframe: pd.DataFrame, columns: List[str]) -> None:
        chart = chart_type.classname(dataframe, chart_type.title + columns[0], columns)
        chart.plot()
