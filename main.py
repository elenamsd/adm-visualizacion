import os
from typing import List

import pandas as pd
from matplotlib import pyplot as plt

from strategies.csv_strategy import CSVStrategy
from strategies.datasource import Datasource

GUARD_NAME = 'dyfed-powys'
GUARD_FOLDER = 'data/' + GUARD_NAME


def get_files() -> List:
    files = []
    for folder in os.listdir(GUARD_FOLDER):
        if os.path.isdir(os.path.join(GUARD_FOLDER, folder)):
            for file in os.listdir(os.path.join(GUARD_FOLDER, folder)):
                if file.endswith('.csv') and not file.startswith('output'):
                    files.append(os.path.join(GUARD_FOLDER, folder, file))

    return files


# def bar_chart(dataframe: pd.DataFrame, x_label: str):
#
#     dataframe.plot.bar(x=x_label, y=y_label, rot=0)
#     plt.show()

def bar_chart(dataframe: pd.DataFrame, x_label: str):
    gender_counts = dataframe[x_label].value_counts()

    gender_counts.plot.bar(rot=0)
    plt.show()


if __name__ == '__main__':
    files = get_files()
    datasource = Datasource(CSVStrategy())
    dataframe = datasource.get_dataframe(files)

    bar_chart(dataframe, 'Gender')
    dataframe.to_csv(GUARD_FOLDER + '/output.csv')
