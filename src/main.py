import requests
import pandas as pd


def computing_the_trip_duration(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Computing the trip duration by using the difference between: pickup_datetime and dropoff_datetime
    and adding the computation to a new column, Then adding this new column the data frame.
    finally the result data frame is returned from the function.

    :param data_frame: original data frame.
    :return: data frame with new column.
    """
    pass


def adding_hours_of_day_and_days_of_week(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Adding two columns to the original data frame the first column is:
    the hour of the day, and the second column is: the day of the week, from the field pickup_datetime.
    finally The new data frame is returned from the function.

    :param data_frame: original data frame.
    :return: data frame with new two columns.
    """
    pass


def computes_predictions(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Computes a new data frame called predictions where the index is:

    - PULocationID.
    - DOLocationID.
    - Day of the week.
    - Hour of the day.

    and has two columns:

    - The mean trip duration.
    - The margin of error (using 95% confidence interval).

    the mean is computed for all trip durations for the same PULocationID / DOLocationID
    /Day of the week / Hour of the day.
    the new data frame is returned from the function.

    :param data_frame: Original Data Frame
    :return: New Data Frame
    """
    pass


def get_predictions(data_url: str) -> pd.DataFrame:
    """
    Reads data file and calling three functions:

    - computing the trip duration function
    - adding the hour of day and the day of week function
    - computes the predictions function

    to generate the data frame called predictions.

    :param data_url: data set API URL
    :return: new data frame called Predictions.
    """
    pass


if __name__ == '__main__':
    url = 'https://data.cityofnewyork.us/resource/4p5c-cbgn.json'

    response = requests.get(url=url)

    data = response.json()

    df = pd.DataFrame(data)

    print(df.shape)
