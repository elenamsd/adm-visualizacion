from typing import List

import numpy as np
import pandas as pd

from src.framework.enum.chart_type import ChartType
from src.framework.enum.datasource_type import DatasourceType
from src.framework.factory.dataframe_factory import DataframeFactory


def datasource_selector() -> pd.DataFrame:
    print('¿Qué fuente de datos desea usar?')
    print('0. Salir')
    for index, datasource_type in enumerate(DatasourceType.list(), start=1):
        print(f"{index}. {datasource_type.name}")

    print('Por favor, seleccione una opción: ', end='')
    option: str = input()

    if option == '0':
        print('Saliendo...')
        exit()
    else:
        try:
            datasource_type: DatasourceType = DatasourceType.list()[int(option) - 1]
            print(f"Ha seleccionado: {datasource_type.name}\n")
            return DataframeFactory.create_dataframe(datasource_type)

        except IndexError:
            print('Opción no válida\n')
            return datasource_selector()
        except ValueError as error:
            print(f"Excepción: {error}\n")
            return datasource_selector()


def chart_selector(full_dataframe: pd.DataFrame) -> None:
    print('\n¿Qué gráfico desea visualizar?')
    print('0. Salir')
    for index, chart_type in enumerate(ChartType.list(), start=1):
        print(f"{index}. {chart_type.name}")

    print('Por favor, seleccione una opción: ', end='')
    option: str = input()

    while option != '0':
        try:
            chart_type: ChartType = ChartType.list()[int(option) - 1]
            print(f"Ha seleccionado: {chart_type.name}")

            dataframe: pd.DataFrame = year_selector(full_dataframe)
            columns: List[str] = columns_selector(dataframe)

            chart = chart_type.classname(dataframe, chart_type.title, columns)
            chart.plot()

            chart_selector(full_dataframe)

        except IndexError:
            print('Opción no válida')
            chart_selector(full_dataframe)
        except ValueError as error:
            print(f"Excepción: {error}")
            chart_selector(full_dataframe)

    print('Saliendo...')
    exit()


def year_selector(dataframe: pd.DataFrame) -> pd.DataFrame:
    if 'Date' not in dataframe.columns:
        return dataframe

    print('\n¿Desea ver un año en concreto o visualizarlos todos?')
    years: np.ndarray = np.sort(dataframe['Date'].dt.year.unique())
    print("0. Todos")
    for index, year in enumerate(years, start=1):
        print(f"{index}. {year}")

    print('Por favor, seleccione una opción: ', end='')
    option: str = input()

    try:
        return dataframe if option == '0' \
            else dataframe[dataframe['Date'].dt.year == years[int(option) - 1]]

    except IndexError:
        print('Opción no válida')
        return year_selector(dataframe)


def columns_selector(dataframe: pd.DataFrame) -> List[str]:
    print('\nSeleccione las columnas que desea visualizar:')
    for index, column in enumerate(dataframe.columns):
        print(f'{index + 1}. {column}')

    print('Por favor, seleccione una columna (separadas por comas): ', end='')
    option: str = input()
    columns: List[str] = []
    try:
        for column in option.split(','):
            columns.append(dataframe.columns[int(column) - 1])
        print(f"Las columnas seleccionadas son: {columns}")
        return columns

    except IndexError:
        print('Opción no válida')
        return columns_selector(dataframe)
    except ValueError as error:
        print(f"Excepción: {error}")
        return columns_selector(dataframe)
