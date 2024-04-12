import os
from typing import List
import pandas as pd
from matplotlib import pyplot as plt
from charts import bar_chart, line_chart, histogram, scatter_plot
from strategies.csv_strategy import CSVStrategy
from strategies.datasource import Datasource

GUARD_NAME = 'dyfed-powys'
GUARD_FOLDER = 'data/' + GUARD_NAME


def get_files() -> List:
    files: List[str] = []
    for folder in os.listdir(GUARD_FOLDER):
        if os.path.isdir(os.path.join(GUARD_FOLDER, folder)):
            for file in os.listdir(os.path.join(GUARD_FOLDER, folder)):
                if file.endswith('.csv') and not file.startswith('output'):
                    files.append(os.path.join(GUARD_FOLDER, folder, file))

    return files

def clean_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe = dataframe.drop(columns=['Part of a policing operation', 'Policing operation', 'Legislation', 'Outcome linked to object of search', 'Removal of more than just outer clothing'])
    dataframe = dataframe.drop(columns=['Latitude', 'Longitude'])
    dataframe = dataframe.dropna(axis=0, how='any')

    dataframe['Date'] = pd.to_datetime(dataframe['Date'])

    print(dataframe.info())
    return dataframe


def count_entries_by_gender(dataframe: pd.DataFrame, gender_label: str) -> pd.DataFrame:
    return dataframe[gender_label].value_counts()


def count_entries_by_year(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe_grouped = dataframe.groupby(dataframe['Date'].dt.year)
    return dataframe_grouped.size()


def count_entries_by_gender_age_and_object_search(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.groupby(['Gender', 'Age range', 'Object of search']).size().reset_index(name='Frequency')


if __name__ == '__main__':
    files: List[str] = get_files()
    datasource: Datasource = Datasource(CSVStrategy())
    dataframe: pd.DataFrame = datasource.get_dataframe(files)

    dataframe = clean_dataframe(dataframe)

    bar_chart(count_entries_by_gender(dataframe, 'Gender'), 'Bar chart ofStops by gender', 'Gender', 'Frecuency')
    line_chart(count_entries_by_year(dataframe), 'Line chart of Stops by year', 'Year', 'Frecuency')
    histogram(dataframe['Age range'], 'Histogram of Stops by age range', 'Age range', 'Frecuency')
    scatter_plot(dataframe, 'ScatterPlot of Stops by gender, age range and object of search')

    # dataframe.to_csv(GUARD_FOLDER + '/output.csv')
