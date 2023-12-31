<p align="center">
<a href="https://github.com/IsmaelMousa/predict-trip-duration/actions/workflows/makefile.yml" alt="...">
        <img src="https://img.shields.io/badge/Makefile_CI-passing-dark_green?logo=github" /></a>
<a href="https://github.com/IsmaelMousa/predict-trip-duration/blob/main/pyproject.toml" alt="...">
        <img src="https://img.shields.io/badge/Poetry-packaging-dark_green?logo=poetry" /></a>
<a href="https://github.com/IsmaelMousa/predict-trip-duration/blob/main/Makefile" alt="...">
        <img src="https://img.shields.io/badge/Makefile-building-blue" /></a>
<a href="https://flake8.pycqa.org/en/latest/" alt="...">
        <img src="https://img.shields.io/badge/Flake8-linter-dark_green?logo=flake8" /></a>

# Predict the trip duration

## Table of contents

* [General Info](#general-info)
* [Technologies](#technologies)
* [Usage](#usage)
* [Description & Functions](#description)
    * [1st Function](#compute-and-add-trip-duration)
    * [2nd Function](#add-hour-of-day-and-day-of-week)
    * [3rd Function](#compute-predictions)
    * [4th Function](#get-predictions)
* [Data Set used](#data-set-used-from-nyc-opendata-thank-you)

## General info

Applying the statistical analysis using python,
We would like to predict trip duration from a location to another using a taxi.

## Technologies

- Python 3.11.2
- Jupyter 1.0.0
- Poetry 1.6.1

## Usage

Download data 7.5GB, if you don't want to use the whole data you can skip this

```Bash
make download
```

Install required dependencies

```Bash
make install
```

Run `main.py` by using code editor (e.g., PyCharm, Visual Studio Code, etc.).

Run `main.ipynb` by using code editor (e.g., DataSpell, Visual Studio Code, etc.).

## Description

We need to write four functions to do some operation on a data set
to generate a dataframe that called predictions, and these predictions is all about the mean value of the trip duration
according of some conditions such as the location, time, and so on.

[2019 High Volume FHV Trip Records](https://data.cityofnewyork.us/Transportation/2019-High-Volume-FHV-Trip-Records/4p5c-cbgn/data)

 hvfhs_license_num | dispatching_base_num | pickup_datetime         | dropoff_datetime        | PULocationID | DOLocationID | SR_Flag 
-------------------|----------------------|-------------------------|-------------------------|--------------|--------------|---------
 HV0002            | B02914               | 2019 Feb 01 12:10:09 AM | 2019 Feb 01 12:31:04 AM | 161          | 33           |
 HV0005            | B02510               | 2019 Feb 01 12:59:55 AM | 2019 Feb 01 01:06:28 AM | 198          | 198          | 1       

### [compute and add trip duration](functions/first.py)

This function takes a dataframe and computes the trip duration by using the difference between
`pickup_datetime` and `dropoff_datetime`, and the computed trip duration will be added as a new column
called `trip_duration`.

The new column is added to the data frame and the result data frame is returned from the function.

### [add hour of day and day of week](functions/second.py)

This function takes a dataframe and adding to it two columns: `hour_of_day` and `day_of_week` from `pickup_datetime`
field.

The new data frame is returned from the function.

### [compute predictions](functions/third.py)

This function computes a new data frame called `predictions` where the index is:

- `PULocationID`
- `DOLocationID`
- `hour_of_day`
- `day_of_week`

And has two columns:

- The mean of trip duration: `mean_trip_duration`
- The margin of error using 95% confidence interval: `margin_of_error`

The mean is computed for all trip durations for the same: **PULocationID** /**DOLocationID** /**hour of day** /**day of
week**.

The new data frame is returned from the function.

### [get predictions](functions/fourth.py)

This function reads the **data file** and calling three functions:

- `compute and add trip duration`
- `add hour of day and day of week`
- `compute predictions`

finally to generate a data frame that is called `predictions`.

### Data Set used from [NYC OpenData](https://opendata.cityofnewyork.us) Thank You!

