import requests as r
import pandas as pd

class EpexSpot():

    def __init__(self):
        self.url = 'https://api.awattar.at/v1/marketdata?'

    def get_spot_prices(self, start, end):

        start_timestamp = int(start.timestamp())
        end_timestamp = int(end.timestamp())

        if start_timestamp > end_timestamp:
            raise Exception("Start must be smaller than end!")

        response = r.get(url= self.url + f'start={start_timestamp}000&end={end_timestamp}000')
        response_df = pd.DataFrame(response.json()['data'])
        response_df['start_date'] = pd.to_datetime(response_df.start_timestamp, unit='ms')


        return response_df[['start_date', 'marketprice', 'unit']]
