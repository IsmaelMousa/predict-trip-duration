# Predict the trip duration

## Table of contents

* [General Info](#general-info)
* [Technologies](#technologies)
* [Usage](#usage)
  * [Install Dependencies](#installing-required-dependencies)
  * [Run Program](#running-the-program)
* [Description & Functions](#description)
  * [1st Function](#1st-function)
  * [2nd Function](#2nd-function)
  * [3rd Function](#3rd-function)
  * [4th Function](#4th-function)
* [Data Set used](#data-set-used-from-nyc-opendata-thank-you)

## General info

Practice inferential statistics using python,
We would like to predict trip duration from a location to another using a taxi.


The idea for this project was proposed by [Dr.Ayser Armiti](https://www.linkedin.com/in/ayserarmiti?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) 
in the Data Science 2 course at An-Najah National University.

## Technologies
* Python 3.11.2
* Poetry 1.6.1

## Usage

### Installing required dependencies
```Bash
# from the terminal type:

make install
```

### Running the program
```Bash
# from the terminal type:

make run-py

# or

make run-ipynb


# or by using code editor (e.g., Pycharm, VS Code, etc.).
```

## Description:
We need to write four functions to do some operation on a data set
to finally generate a dataframe that is called predictions.

Data Set that we used: [2019 High Volume FHV Trip Records](https://data.cityofnewyork.us/Transportation/2019-High-Volume-FHV-Trip-Records/4p5c-cbgn/data)

### 1st Function

This Function takes a dataframe and computes the trip duration using the difference between pickup_datetime and dropoff_datetime.
The new column is added to the data frame and the result data frame is returned from the function.
### 2nd Function

This Function takes a data frame and adds to it the hour of the day and the day of the week from the field pickup_datetime.
The new data frame is returned from the function.

### 3rd Function

This Function computes a new data frame called predictions where the index is:

* PULocationID.
* DOLocationID.
* Day of the week.
* Hour of the day.

And has two columns:

* The mean trip duration. 
* The margin of error (using 95% confidence interval).

The mean is computed for all trip durations for the same PULocationID / DOLocationID / Day of the week / Hour of the day.
The new data frame is returned from the function.

### 4th Function

This Function reads the data file and calls the three functions to finally generate the data frame that is called predictions.


## Data Set used from [NYC OpenData](https://opendata.cityofnewyork.us) Thank You!

