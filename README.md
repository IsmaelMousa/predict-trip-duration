# Predict the trip duration

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Usage](#usage)
  * [Install Dependencies](#installing-required-dependencies)
  * [Run Program](#running-the-program)
* [Description](#description)
  * [First Function](#first-function)
  * [Second Function](#second-function)
  * [Third Function](#third-function)
  * [Third Function](#forth-function)
* [Data set used](#data-set-used-from-nyc-opendata-thank-you)

## General info

Practice inferential statistics using python,
We would like to predict trip duration from a location to another using a taxi.

This project is a training and educational project,
as the project was presented in the Data Science 2 course at An-Najah National University.



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

python3 main.py

# Or

jupyter notebook main.ipynb

# Or by using code editor (e.g., Pycharm, Visual Studio Code)
```

## Description:
We need to write four functions to do some operation on a data set
to finally generate a dataframe that is called predictions.

Data Set that we used: [2019 High Volume FHV Trip Records](httpscolabresearchgooglecomcorgiredirectorsitehttps3a2f2fdatacityofnewyorkus2ftransportation2f2019-high-volume-fhv-trip-records2f4p5c-cbgn2fdata-)

### First Function

This Function takes a dataframe and computes the trip duration using the difference between pickup_datetime and dropoff_datetime.
The new column is added to the data frame and the result data frame is returned from the function.
### Second Function

This Function takes a data frame and adds to it the hour of the day and the day of the week from the field pickup_datetime.
The new data frame is returned from the function.

### Third Function

This Function computes a new data frame called predictions where the index is:

* PULocationID
* DOLocationID
* Day of the week
* Hour of the day

And has two columns:

* The mean trip duration 
* The margin of error using 95% confidence interval

The mean is computed for all trip durations for the same PULocationID / DOLocationID / Day of the week / Hour of the day.
The new data frame is returned from the function.

### Forth Function

This Function that read the data file and calls the three functions to finally generate the data frame that is called predictions.


## Data Set used from [NYC OpenData](https://opendata.cityofnewyork.us) Thank You!

