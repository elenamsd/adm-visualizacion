import os
from strategies.csv_strategy import CSVStrategy
from strategies.datasource import Datasource

GUARD_NAME = 'dyfed-powys'
GUARD_FOLDER = 'data/' + GUARD_NAME


def get_files():
    files = []
    for folder in os.listdir(GUARD_FOLDER):
        if os.path.isdir(os.path.join(GUARD_FOLDER, folder)):
            for file in os.listdir(os.path.join(GUARD_FOLDER, folder)):
                if file.endswith('.csv') and not file.startswith('output'):
                    files.append(os.path.join(GUARD_FOLDER, folder, file))

    return files


if __name__ == '__main__':
    files = get_files()
    datasource = Datasource(CSVStrategy())
    dataframe = datasource.get_dataframe(files)
    dataframe.to_csv(GUARD_FOLDER + '/output.csv')
