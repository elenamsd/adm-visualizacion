from abc import abstractmethod

from src.framework.chart.chart import Chart


class Model(Chart):

    @abstractmethod
    def algorithm(self):
        pass
