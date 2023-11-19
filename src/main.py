import requests
import pandas as pd


def computing_the_trip_duration(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    TODO: write docs
    :param data_frame: Original Data Frame
    :return: New Data Frame
    """
    pass


def adding_hours_of_day_and_days_of_week(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    TODO: write docs
    :param data_frame: Original Data Frame
    :return: New Data Frame
    """
    pass


def computes_predictions(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    TODO: write docs
    :param data_frame: Original Data Frame
    :return: New Data Frame
    """
    pass


def get_predictions(url: str) -> pd.DataFrame:
    """
    TODO: write docs
    :param url: Dataset API URL
    :return: Predictions
    """
    pass


if __name__ == '__main__':
    url = 'https://data.cityofnewyork.us/resource/4p5c-cbgn.json'

    response = requests.get(url=url)

    data = response.json()

    df = pd.DataFrame(data)
