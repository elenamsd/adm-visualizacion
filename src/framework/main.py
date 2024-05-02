import pandas as pd

from src.framework.enum.chart_type import ChartType
from src.framework.enum.datasource_type import DatasourceType
from src.framework.factory.chart_factory import ChartFactory
from src.framework.factory.dataframe_factory import DataframeFactory


def count_entries_by_gender(dataframe: pd.DataFrame, gender_label: str) -> pd.DataFrame:
    return dataframe[gender_label].value_counts()


def count_entries_by_year(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe_grouped = dataframe.groupby(dataframe['Date'].dt.year)
    return dataframe_grouped.size()


def count_entries_by_gender_age_and_object_search(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.groupby(['Gender', 'Age range', 'Object of search']).size().reset_index(name='Frequency')


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

        except (ValueError, IndexError):
            print('Opción no válida\n')
            return datasource_selector()


def chart_selector(dataframe: pd.DataFrame) -> None:
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
            ChartFactory.create_chart(chart_type, dataframe)
            chart_selector(dataframe)

        except (ValueError, IndexError):
            print('\nOpción no válida')
            chart_selector(dataframe)


    print('Saliendo...')
    exit()


if __name__ == '__main__':
    dataframe: pd.DataFrame = datasource_selector()

    if dataframe.empty:
        print('No se han encontrado datos')
        exit()

    print(dataframe.info())

    chart_selector(dataframe)

    # bar_chart(count_entries_by_gender(dataframe, 'Gender'), 'Bar chart of Stops by gender', 'Gender', 'Frecuency')
    # line_chart(count_entries_by_year(dataframe), 'Line chart of Stops by year', 'Year', 'Frecuency')
    # histogram(dataframe['Age range'], 'Histogram of Stops by age range', 'Age range', 'Frecuency')
    # scatter_plot(dataframe, 'ScatterPlot of Stops by gender, age range and object of search')

    # dataframe.to_csv(GUARD_FOLDER + '/output.csv')
