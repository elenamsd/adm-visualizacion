import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


def line_chart(dataframe: pd.DataFrame, title: str, x_label: str, y_label: str) -> None:
    plt.plot(dataframe.index, dataframe.values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def histogram(dataframe: pd.DataFrame, title: str, x_label: str, y_label: str) -> None:
    plt.hist(dataframe)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def scatter_plot(dataframe: pd.DataFrame, title: str) -> None:
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=dataframe, x='Age range', y='Gender', hue='Object of search')
    plt.title(title)
    plt.show()
