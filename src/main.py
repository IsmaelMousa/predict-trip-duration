import pandas as pd


def compute_trip_duration(original_df: pd.DataFrame) -> pd.DataFrame:
    """
    Computing the trip duration by using the difference between:
    pickup_datetime and dropoff_datetime
    and adding the computation to a new column called: trip_duration,
    then adding this new column the data frame.

    finally the result data frame is returned from the function.

    :param original_df: original data frame.
    :return: data frame with new column.
    """

    original_df.pickup_datetime = pd.to_datetime(original_df.pickup_datetime)
    original_df.dropoff_datetime = pd.to_datetime(original_df.dropoff_datetime)

    trip_duration = ((original_df.dropoff_datetime - original_df.pickup_datetime).dt.total_seconds() / 60).round(2)

    original_df.insert(loc=4, column='trip_duration', value=trip_duration)

    return original_df


def add_hour_of_day_and_day_of_week_columns(original_df: pd.DataFrame) -> pd.DataFrame:
    """
    Adding two columns to the original data frame the first column is:
    the hour of day, and the second column is: the day of week,
    from the field pickup_datetime.
    finally The new data frame is returned from the function.

    :param original_df: original data frame.
    :return: data frame with new two columns.
    """

    original_df.pickup_datetime = pd.to_datetime(original_df.pickup_datetime)

    hour_of_day = original_df.pickup_datetime.dt.hour
    day_of_week = original_df.pickup_datetime.dt.day_name()

    original_df.insert(loc=5, column='hour_of_day', value=hour_of_day)
    original_df.insert(loc=6, column='day_of_week', value=day_of_week)

    return original_df


def compute_predictions(original_df: pd.DataFrame) -> pd.DataFrame:
    """
    Computing a new data frame called predictions where the index is:

    - pulocationid
    - dolocationid
    - day of week
    - hour of day

    and has two columns:

    - The mean of trip duration
    - The margin of error (using 95% confidence interval)

    the mean is computed for all trip durations for the same pulocationid / dolocationid
    /day of week /hour of day.
    the new data frame is returned from the function.

    :param original_df: original data frame.
    :return: new data frame called predictions.
    """

    grouped_df = original_df.groupby(['pulocationid', 'dolocationid', 'hour_of_day', 'day_of_week'])

    mean_trip_duration = grouped_df.trip_duration.mean().round(2)

    predictions = pd.DataFrame(mean_trip_duration).reset_index()

    predictions.set_index(keys=['pulocationid', 'dolocationid', 'hour_of_day', 'day_of_week'], inplace=True)
    predictions.rename(columns={'trip_duration': 'mean_trip_duration'}, inplace=True)

    return predictions

    # predictions = original_df[['pulocationid', 'dolocationid', 'hour_of_day', 'day_of_week', 'trip_duration']].copy()
    #
    # predictions.set_index(['pulocationid', 'dolocationid', 'hour_of_day', 'day_of_week'], inplace=True)
    #
    # predictions = predictions.groupby(
    #     ['pulocationid', 'dolocationid', 'hour_of_day', 'day_of_week']).mean(numeric_only=True).round(2)
    #
    # predictions.rename(columns={'trip_duration': 'mean_trip_duration'}, inplace=True)
    #
    # return predictions


def get_predictions(path: str) -> pd.DataFrame:
    """
    Reading the data file and calling three functions:

    - computing the trip duration function
    - adding the hour of day and the day of week function
    - computes the predictions function

    to generate the data frame called predictions.

    :param path: data file path
    :return: new data frame called Predictions.
    """
    original_df = pd.read_csv(filepath_or_buffer=path)

    compute_trip_duration(original_df=original_df)

    add_hour_of_day_and_day_of_week_columns(original_df=original_df)

    predictions = compute_predictions(original_df=original_df)

    return predictions


if __name__ == '__main__':
    df = pd.read_csv('sample.csv')

    a = compute_trip_duration(original_df=df)
    print(a.head(2).to_string(index=False), '\n')

    b = add_hour_of_day_and_day_of_week_columns(original_df=df)
    print(b.head(2).to_string(index=False), '\n')

    c = compute_predictions(original_df=df)
    print(c.head(2).to_string(index=False), '\n')
