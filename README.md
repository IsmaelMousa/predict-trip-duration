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

Practice inferential statistics using python,
We would like to predict trip duration from a location to another using a taxi.


The idea for this project was proposed by [Dr.Ayser Armiti](https://www.linkedin.com/in/ayserarmiti?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) 
in the Data Science 2 course at An-Najah National University.

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
to generate a dataframe that is called predictions.

Data Set that we used: [2019 High Volume FHV Trip Records](https://data.cityofnewyork.us/Transportation/2019-High-Volume-FHV-Trip-Records/4p5c-cbgn/data)

### compute and add trip duration
This function takes a dataframe and computes the trip duration by using the difference between
`pickup_datetime` and `dropoff_datetime`, and the computed trip duration will be added as a new column called `trip_duration`.

The new column is added to the data frame and the result data frame is returned from the function.

### add hour of day and day of week

This function takes a dataframe and adding to it two columns: `hour_of_day` and `day_of_week` from `pickup_datetime` field.

The new data frame is returned from the function.

### compute predictions

This function computes a new data frame called `predictions` where the index is:

- `PULocationID`
- `DOLocationID`
- `hour_of_day`
- `day_of_week`

And has two columns:

- The mean of trip duration: `mean_trip_duration`  
- The margin of error using 95% confidence interval: `margin_of_error`

The mean is computed for all trip durations for the same: **PULocationID** /**DOLocationID** /**hour of day** /**day of week**.

The new data frame is returned from the function.

### get predictions
This function reads the **data file** and calling three functions:

- `compute and add trip duration`
- `add hour of day and day of week`
- `compute predictions`

Finally to generate a data frame  that is called `predictions`.

### Data Set used from [NYC OpenData](https://opendata.cityofnewyork.us) Thank You!

