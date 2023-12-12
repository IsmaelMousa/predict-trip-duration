import pandas as pd
from scipy.stats import norm


def compute_and_add_trip_duration(original_df: pd.DataFrame) -> pd.DataFrame:
    """
    Computing the trip duration by using the difference between:
    pickup_datetime and dropoff_datetime (in Minutes).
    and the computed trip duration will be added as a new column called: trip_duration,
    and this new column will be added to the original data frame.

    finally the result data frame is returned from the function.

    :param original_df: original data frame
    :return: the original data frame with new column
    """

    pick_up_datetime = pd.to_datetime(arg=original_df.pickup_datetime)
    drop_off_datetime = pd.to_datetime(arg=original_df.dropoff_datetime)

    trip_duration = ((drop_off_datetime - pick_up_datetime).dt.total_seconds() / 60).round(2)

    original_df.insert(loc=4, column='trip_duration', value=trip_duration)

    return original_df


def add_hour_of_day_and_day_of_week(original_df: pd.DataFrame) -> pd.DataFrame:
    """
    Adding two columns to the original data frame where the first column:
    hour of day, and the second column: day of week from pickup_datetime field.

    finally the new data frame is returned from the function.

    :param original_df: original data frame
    :return: the original data frame with new two columns
    """

    hour_of_day = pd.to_datetime(arg=original_df.pickup_datetime).dt.hour
    day_of_week = pd.to_datetime(arg=original_df.pickup_datetime).dt.day_name()

    original_df.insert(loc=5, column='hour_of_day', value=hour_of_day)
    original_df.insert(loc=6, column='day_of_week', value=day_of_week)

    return original_df


def compute_predictions(original_df: pd.DataFrame) -> pd.DataFrame:
    """
    Computing a new data frame called predictions where the index is:

    - PULocationID
    - DOLocationID
    - hour of day
    - day of week

    and has two columns:

    - mean trip duration
    - margin of error

    the mean is computed for all trip durations for the same:
    PULocationID / DOLocationID /day of week /hour of day.
    the new data frame is returned from the function.

    :param original_df: original data frame
    :return: new data frame called predictions
    """

    predictions = (original_df.groupby(by=['PULocationID', 'DOLocationID', 'hour_of_day', 'day_of_week'])
                   .aggregate(mean_trip_duration=('trip_duration', 'mean'), margin_of_error=('trip_duration', 'sem')))

    z_score = norm.ppf(q=0.975)

    standard_error = predictions.margin_of_error

    predictions.margin_of_error = (z_score * standard_error).round(2)

    return predictions


def get_predictions(file_path: str) -> pd.DataFrame:
    """
    Reading the data file and calling three functions:

    - compute and add trip duration
    - add hour of day and day of week
    - compute predictions

    finally to generate a new data frame called predictions.

    :param file_path: dataset file path
    :return: generated data frame called predictions
    """

    original_df = pd.read_csv(filepath_or_buffer=file_path)

    compute_and_add_trip_duration(original_df=original_df)

    add_hour_of_day_and_day_of_week(original_df=original_df)

    predictions = compute_predictions(original_df=original_df)

    return predictions


if __name__ == '__main__':
    pass
