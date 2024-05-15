import pandas as pd

from src.framework.handler.handler_strategy import HandlerStrategy


class UKAccidentsHandler(HandlerStrategy):

    def clean_dataframe(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe = dataframe.drop(columns=['Unnamed: 0', 'Accident_Index', 'Location_Easting_OSGR', 'Location_Northing_OSGR', 'Police_Force',
                                            'Day_of_Week', 'Local_Authority_(District)', 'Local_Authority_(Highway)', '1st_Road_Number',
                                            '2nd_Road_Class', '2nd_Road_Number', 'Pedestrian_Crossing-Human_Control', 'Special_Conditions_at_Site',
                                            'Carriageway_Hazards', 'LSOA_of_Accident_Location', 'Year'])
        dataframe['Junction_Control'].fillna('Uncontrolled', inplace=True)
        dataframe = dataframe.dropna()

        dataframe['Date'] = pd.to_datetime(dataframe['Date'], format='%d/%m/%Y')

        return dataframe
