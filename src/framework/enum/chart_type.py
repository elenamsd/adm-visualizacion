from enum import Enum
from typing import List, Type

from src.framework.chart.bar_chart import BarChart
from src.framework.chart.chart import Chart
from src.framework.chart.line_chart import LineChart


class ChartType(Enum):

    BAR_CHART = ("Bar chart", BarChart, "Bar chart by ")
    LINE_CHART = ("Line chart", LineChart, "Line chart by ")
    HISTOGRAM = ("Histogram", BarChart, "Histogram by ")
    SCATTER_PLOT = ("Scatter plot", BarChart, "Scatter plot by ")

    def __new__(cls, name: str, classname: Type[Chart], title: str) -> Enum:
        chart_type = object.__new__(cls)
        chart_type._name = name
        chart_type._classname = classname
        chart_type._title = title
        return chart_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def classname(self) -> Type[Chart]:
        return self._classname

    @property
    def title(self) -> str:
        return self._title

    @classmethod
    def list(cls) -> List['ChartType']:
        return [chart_type for chart_type in cls]

    def is_bar_chart(self) -> bool:
        return self == ChartType.BAR_CHART

    def is_line_chart(self) -> bool:
        return self == ChartType.LINE_CHART

    def is_histogram(self) -> bool:
        return self == ChartType.HISTOGRAM

    def is_scatter_plot(self) -> bool:
        return self == ChartType.SCATTER_PLOT
