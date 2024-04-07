import pandas as pd

LISTINGS_FILE = 'data/'
REVIEWS_FILE = 'data/'

def get_dataframe_from(file):
    return pd.read_csv(file)


if __name__ == '__main__':
    listings_df = get_dataframe_from(LISTINGS_FILE)
    reviews_df = get_dataframe_from(REVIEWS_FILE)

    df = listings_df.merge(reviews_df, left_on='id', right_on='listing_id')

    print(listings_df.columns)
    print(reviews_df.columns)

    print(df)

    df.to_csv('output.csv')

