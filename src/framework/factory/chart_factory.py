from typing import List

import pandas as pd

from src.framework.enum.chart_type import ChartType


class ChartFactory:

    @staticmethod
    def create_chart(chart_type: ChartType, dataframe: pd.DataFrame) -> None:
        try:
            columns: List[str] = ChartFactory._select_columns(dataframe)
            return ChartFactory._create_bidimensional_chart(chart_type, dataframe, columns)
        except (ValueError, IndexError):
            raise ValueError('Invalid chart type')

    @classmethod
    def _select_columns(cls, dataframe: pd.DataFrame) -> List[str]:
        print('\nSeleccione las columnas que desea visualizar:')
        for index, column in enumerate(dataframe.columns):
            print(f'{index + 1}. {column}')

        print('Por favor, seleccione una columna (separadas por comas): ', end='')
        option: str = input()
        columns: List[str] = []
        for column in option.split(','):
            columns.append(dataframe.columns[int(column) - 1])

        print(f"Las columnas seleccionadas son: {columns}")
        if not all(column in dataframe.columns for column in columns):
            print('\nAlguna de las columnas seleccionadas no existe en el dataframe.')
            return ChartFactory._select_columns(dataframe)

        return columns

    @classmethod
    def _create_bidimensional_chart(cls, chart_type: ChartType, dataframe: pd.DataFrame, columns: List[str]) -> None:
        if len(columns) != 1:
            raise ValueError(f"{chart_type.name} only supports one column")

        chart = chart_type.classname(dataframe, chart_type.title + columns[0], columns)
        chart.plot()
