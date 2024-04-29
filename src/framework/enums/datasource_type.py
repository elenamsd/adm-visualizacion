from enum import Enum


class DatasourceType(Enum):

    DYFED_POWYS_STOP_AND_SEARCH = "stop_and_search", "Dyfed Powys - Stop and Search", "../../data/dyfed-powys/"

    def __new__(cls, name, description, path):
        datasource = object.__new__(cls)
        datasource._name = name
        datasource._description = description
        datasource._path = path
        return datasource

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def path(self):
        return self._path
