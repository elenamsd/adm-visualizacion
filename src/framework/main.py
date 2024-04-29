from typing import List
import pandas as pd
from src.framework.charts import bar_chart, line_chart, histogram, scatter_plot
from src.framework.enums.datasource_type import DatasourceType
from src.framework.handler.strategy.handler_context import HandlerContext
from src.framework.reader.strategy.impl.stop_and_search_csv_reader import StopAndSearchCsvReader
from src.framework.reader.strategy.reader_context import ReaderContext

from src.framework.handler.factory.handler_factory import HandlerFactory

GUARD_NAME = 'dyfed-powys'
DATA_FOLDER = '../../data/'


def count_entries_by_gender(dataframe: pd.DataFrame, gender_label: str) -> pd.DataFrame:
    return dataframe[gender_label].value_counts()


def count_entries_by_year(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe_grouped = dataframe.groupby(dataframe['Date'].dt.year)
    return dataframe_grouped.size()


def count_entries_by_gender_age_and_object_search(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.groupby(['Gender', 'Age range', 'Object of search']).size().reset_index(name='Frequency')


def menu():
    print('¿Qué fuente de datos desea usar?')
    print('0. Salir')
    print('1. ' + DatasourceType.DYFED_POWYS_STOP_AND_SEARCH.description)
    print('Por favor, seleccione una opción: ', end='')
    option = input()
    if option == '0':
        print('Saliendo...')
        exit()
    elif option == '1':
        print('Ha seleccionado ' + DatasourceType.DYFED_POWYS_STOP_AND_SEARCH.description)
        reader: ReaderContext = ReaderContext(StopAndSearchCsvReader())
        dataset: List[str] = reader.get_files(DATA_FOLDER + GUARD_NAME)
        dataframe: pd.DataFrame = reader.get_dataframe(dataset)

        handler: HandlerContext = HandlerFactory.create_handler(DatasourceType.DYFED_POWYS_STOP_AND_SEARCH.name)

        dataframe_cleaned: pd.DataFrame = handler.clean_dataframe(dataframe)

        return dataframe_cleaned
    else:
        print('Opción no válida')
        menu()

if __name__ == '__main__':
    # reader: ReaderContext = ReaderContext(StopAndSearchCsvReader())
    # dataset: List[str] = reader.get_files(DATA_FOLDER + GUARD_NAME)
    # dataframe: pd.DataFrame = reader.get_dataframe(dataset)

    # handler: HandlerContext = HandlerContext(StopAndSearchHandler())
    # dataframe_cleaned: pd.DataFrame = handler.clean_dataframe(dataframe)

    dataframe_cleaned = menu()

    bar_chart(count_entries_by_gender(dataframe_cleaned, 'Gender'), 'Bar chart of Stops by gender', 'Gender', 'Frecuency')
    line_chart(count_entries_by_year(dataframe_cleaned), 'Line chart of Stops by year', 'Year', 'Frecuency')
    histogram(dataframe_cleaned['Age range'], 'Histogram of Stops by age range', 'Age range', 'Frecuency')
    scatter_plot(dataframe_cleaned, 'ScatterPlot of Stops by gender, age range and object of search')

    # dataframe.to_csv(GUARD_FOLDER + '/output.csv')
