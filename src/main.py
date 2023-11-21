import pandas as pd


def computing_the_trip_duration(original_df: pd.DataFrame) -> pd.DataFrame:
    """
    Computing the trip duration by using the difference between:
    pickup_datetime and dropoff_datetime
    and adding the computation to a new column, Then adding this new column the data frame.
    finally the result data frame is returned from the function.

    :param original_df: original data frame.
    :return: data frame with new column.
    """

    original_df['pickup_datetime'] = pd.to_datetime(original_df['pickup_datetime'])
    pick_up_time = original_df['pickup_datetime']

    original_df['dropoff_datetime'] = pd.to_datetime(original_df['dropoff_datetime'])
    drop_off_time = original_df['dropoff_datetime']

    trip_duration = ((drop_off_time - pick_up_time).dt.total_seconds() / 60).round(2)

    original_df.insert(loc=4, column='trip_duration', value=trip_duration)

    return original_df


def adding_hour_of_day_and_day_of_week(original_df: pd.DataFrame) -> pd.DataFrame:
    """
    Adding two columns to the original data frame the first column is:
    the hour of day, and the second column is: the day of week,
    from the field pickup_datetime.
    finally The new data frame is returned from the function.

    :param original_df: original data frame.
    :return: data frame with new two columns.
    """

    original_df['pickup_datetime'] = pd.to_datetime(original_df['pickup_datetime'])

    hour_of_day = original_df['pickup_datetime'].dt.hour
    day_of_week = original_df['pickup_datetime'].dt.day_of_week

    original_df.insert(loc=5, column='hour_of_day', value=hour_of_day)
    original_df.insert(loc=6, column='day_of_week', value=day_of_week)

    return original_df


def computes_predictions(original_df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes a new data frame called predictions where the index is:

    - PULocationID.
    - DOLocationID.
    - day of the week.
    - hour of the day.

    and has two columns:

    - The mean trip duration.
    - The margin of error (using 95% confidence interval).

    the mean is computed for all trip durations for the same PULocationID / DOLocationID
    /Day of the week / Hour of the day.
    the new data frame is returned from the function.

    :param original_df: original data frame.
    :return: new data frame called predictions.
    """
    pass


def get_predictions(original_df: str) -> pd.DataFrame:
    """
    Reads data file and calling three functions:

    - computing the trip duration function
    - adding the hour of day and the day of week function
    - computes the predictions function

    to generate the data frame called predictions.

    :param original_df: data set API URL
    :return: new data frame called Predictions.
    """
    pass


if __name__ == '__main__':
    path = 'sample.csv'

    df = pd.read_csv(path)

    # 1st
    new_df_with_the_trip_duration = computing_the_trip_duration(original_df=df)

    # 2nd
    new_df_with_hours_of_day_and_days_of_week = adding_hour_of_day_and_day_of_week(original_df=df)
