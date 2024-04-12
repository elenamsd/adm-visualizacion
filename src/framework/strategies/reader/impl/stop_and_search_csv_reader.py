import os
from typing import List
from src.framework.strategies.reader.csv_reader import CsvReader


class StopAndSearchCsvReader(CsvReader):

    def get_files(self, path: str) -> List[str]:
        dataset: List[str] = []
        for folder in os.listdir(path):
            if os.path.isdir(os.path.join(path, folder)):
                for file in os.listdir(os.path.join(path, folder)):
                    if file.endswith('.csv') and not file.startswith('output'):
                        dataset.append(os.path.join(path, folder, file))

        return dataset
