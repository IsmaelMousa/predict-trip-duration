from functions import compute_and_add_trip_duration
from functions import add_hour_of_day_and_day_of_week
from functions import compute_predictions

import pandas as pd


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
