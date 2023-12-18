import pandas as pd


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
