from enum import Enum
from typing import List

DATA_FOLDER = '../../data/'


class DatasourceType(Enum):

    STOP_AND_SEARCH_DYFED_POWYS = ("Dyfed Powys - Stop and Search", f"{DATA_FOLDER}dyfed-powys/")

    def __new__(cls, name, path):
        datasource = object.__new__(cls)
        datasource._name = name
        datasource._path = path
        return datasource

    @property
    def name(self) -> str:
        return self._name

    @property
    def path(self) -> str:
        return self._path

    @classmethod
    def list(cls) -> List['DatasourceType']:
        return [datasource_type for datasource_type in cls]

    def is_dyfed_powys(self) -> bool:
        return self == DatasourceType.STOP_AND_SEARCH_DYFED_POWYS
