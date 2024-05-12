from typing import List

import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from matplotlib import pyplot as plt

from src.framework.chart.chart import Chart


class MapChart(Chart):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        super().__init__(dataframe, title, columns)

    def plot(self) -> None:
        # if len(self.columns) != 3:
        #     raise ValueError("MapChart requires a DataFrame with geometry column.")

        geometry = [Point(xy) for xy in zip(self.dataframe[self.columns[0]], self.dataframe[self.columns[1]])]
        gdf = gpd.GeoDataFrame(self.dataframe, geometry=geometry)

        fig, ax = plt.subplots(figsize=(10, 6))
        world.plot(ax=ax, color='lightgrey')
        gdf.plot(ax=ax, column=self.columns[2], cmap='OrRd', legend=True, legend_kwds={'label': f'{self.columns[2]}'})

        gdf.plot(column=self.columns[1], cmap='OrRd', legend=True)
        plt.title(self.title)
        plt.show()


# import geopandas as gpd
# import pandas as pd
# from matplotlib import pyplot as plt
# from typing import List
# from shapely.geometry import Point
#
# from src.framework.chart.chart import Chart


# class MapChart(Chart):
#     def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
#         super().__init__(dataframe, title, columns)
#
#     def plot(self) -> None:
#         if len(self.columns) < 2:
#             raise ValueError("MapChart necesita al menos 2 columnas: una para la latitud y otra para la longitud")
#
#         # Create a GeoDataFrame from the DataFrame
#         gdf = gpd.GeoDataFrame(self.dataframe, geometry=gpd.points_from_xy(self.dataframe[self.columns[1]], self.dataframe[self.columns[0]]))
#
#         map = gpd.read_file(gdf.get_path('NHS_England_Regions_January_2024_EN_BFC_3616336018640687069.geojson'))
#         # Plot the points
#         gdf.plot(marker='o', color='b', markersize=5, ax=map.plot(figsize=(10, 6)))
#
#         plt.title('Map Chart')
#         plt.show()
