import pandas as pd
from scipy.stats import norm


def compute_predictions(original_df: pd.DataFrame) -> pd.DataFrame | str:
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

    Note: The values of trip duration will be rounded to the nearest two decimal values.

    :param original_df: original data frame
    :return: new data frame called predictions
    """

    try:
        predictions = (original_df.groupby(
            by=['PULocationID', 'DOLocationID', 'hour_of_day', 'day_of_week'])
                       .aggregate(mean_trip_duration=('trip_duration', 'mean'),
                                  margin_of_error=('trip_duration', 'sem')))

        z_score = norm.ppf(q=0.975)

        standard_error = predictions.margin_of_error

        predictions.margin_of_error = (z_score * standard_error).round(2)

        return predictions

    except KeyError as e:
        return f"in {__name__[10:]} function: {e} key is not found!"

    except AttributeError as e:
        return f"in {__name__[10:]} function: {e}!"

    except Exception as e:
        return f"Unhandled exception! in {__name__[10:]} function: {e}!"
