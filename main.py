import os
import pandas as pd

GUARD_NAME = 'dyfed-powys'
GUARD_FOLDER = 'data/' + GUARD_NAME

def get_dataframe():
    dfs = []
    for folder in os.listdir(GUARD_FOLDER):
        if os.path.isdir(os.path.join(GUARD_FOLDER, folder)):
            for file in os.listdir(os.path.join(GUARD_FOLDER, folder)):
                if file.endswith('.csv') and not file.startswith('output'):
                    dfs.append(pd.read_csv(os.path.join(GUARD_FOLDER, folder, file)))

    return pd.concat(dfs, ignore_index=True)


if __name__ == '__main__':
    df = get_dataframe()
    print(df)

    df.to_csv(GUARD_FOLDER + '/output.csv')
