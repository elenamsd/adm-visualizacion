import geopandas as gpd
import geopandas.datasets
import pandas as pd
from geopandas import GeoDataFrame
from matplotlib import pyplot as plt
from typing import List
from src.framework.chart.chart import Chart


class MapChart(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)

    def plot(self) -> None:
        if len(self.columns) < 2:
            raise ValueError("MapChart necesita al menos 2 columnas: una para la latitud y otra para la longitud")

        gdf = GeoDataFrame(self.dataframe, geometry=gpd.points_from_xy(self.dataframe[self.columns[0]], self.dataframe[self.columns[1]]))

        path_to_data = geopandas.datasets.get_path("naturalearth_lowres")
        world = gpd.read_file(path_to_data)

        ax = world[world.name == "United Kingdom"].plot(color='white', edgecolor='black')
        gdf.plot(ax=ax, color='#57078c', markersize=2)

        plt.show()
