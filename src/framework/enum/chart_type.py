from enum import Enum
from typing import List, Type

from src.framework.chart.bar_chart import BarChart
from src.framework.chart.box_plot import BoxPlot
from src.framework.chart.chart import Chart
from src.framework.chart.heat_map import HeatMap
from src.framework.chart.histogram import Histogram
from src.framework.chart.line_chart import LineChart
from src.framework.chart.pair_plot import PairPlot
from src.framework.chart.probability_density_function import ProbabilityDensityFunction
from src.framework.chart.scatter_plot import ScatterPlot
from src.framework.chart.violin_plot import ViolinPlot


class ChartType(Enum):

    BAR_CHART = ("Bar chart", BarChart, "Bar chart by")
    LINE_CHART = ("Line chart", LineChart, "Line chart by")
    HISTOGRAM = ("Histogram", Histogram, "Histogram by")
    SCATTER_PLOT = ("Scatter plot", ScatterPlot, "Scatter plot by")
    HEAT_MAP = ("Heat map", HeatMap, "Heat map by")
    BOX_PLOT = ("Box plot", BoxPlot, "Box plot by")
    VIOLIN_PLOT = ("Violin plot", ViolinPlot, "Violin plot by")
    PROBABILITY_DENSITY_FUNCTION = ("Probability density function", ProbabilityDensityFunction, "Probability density function by")
    PAIR_PLOT = ("Pair plot", PairPlot, "Pair plot by")

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

    def is_heat_map(self) -> bool:
        return self == ChartType.HEAT_MAP

    def is_box_plot(self) -> bool:
        return self == ChartType.BOX_PLOT

    def is_violin_plot(self) -> bool:
        return self == ChartType.VIOLIN_PLOT

    def is_probability_density_function(self) -> bool:
        return self == ChartType.PROBABILITY_DENSITY_FUNCTION

    def is_pair_plot(self) -> bool:
        return self == ChartType.PAIR_PLOT
