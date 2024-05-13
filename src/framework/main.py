import pandas as pd

from src.framework.menu import datasource_selector, chart_selector

if __name__ == '__main__':
    dataframe: pd.DataFrame = datasource_selector()

    if dataframe.empty:
        print('No se han encontrado datos')
        exit()

    print(dataframe.info())

    chart_selector(dataframe)
