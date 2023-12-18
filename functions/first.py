import pandas as pd


def compute_and_add_trip_duration(original_df: pd.DataFrame) -> pd.DataFrame:
    """
    Computing the trip duration by using the difference between:
    pickup_datetime and dropoff_datetime (in Minutes).
    and the computed trip duration will be added as a new column called: trip_duration,
    and this new column will be added to the original data frame.

    finally the result data frame is returned from the function.

    Note: The values of trip duration will be rounded to the nearest two decimal values.

    :param original_df: original data frame
    :return: the original data frame with new column
    """

    pick_up_datetime = pd.to_datetime(arg=original_df.pickup_datetime)
    drop_off_datetime = pd.to_datetime(arg=original_df.dropoff_datetime)

    trip_duration = ((drop_off_datetime - pick_up_datetime)
                     .dt.total_seconds() / 60).round(2)

    original_df.insert(loc=4, column='trip_duration', value=trip_duration)

    return original_df
