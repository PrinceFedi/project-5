# Nose tests #


This code contains unit tests to verify the correctness of the `open_time` and `close_time` functions in the `acp_times.py` module. These functions calculate the opening and closing times for controls along a brevet route given the distance, the maximum distance allowed for the brevet, and the start time.

## Usage
To use this code, ensure that the `acp_times.py` module is in the same directory as the `test_brevet_times.py` file. Then, run the `test_brevet_times.py` file using a Python interpreter, such as with the command python `test_brevet_times.py`.

## Dependencies
This code depends on the `arrow` module for working with date times and the logging module for logging error messages. 

## Files
* `test_brevet_times.py`: The main file containing the unit tests.
* `acp_times.py`: The module containing the `open_time` and `close_time` functions.

## Functions
* `test_brevet_200()`: A unit test for a 200 km brevet distance.
* `test_brevet_300()`: A unit test for a 300 km brevet distance.
* `test_brevet_400()`: A unit test for a 400 km brevet distance.
* `test_brevet_600()`: A unit test for a 600 km brevet distance.
* `test_brevet_1000()`: A unit test for a 1000 km brevet distance.

## Author

Fedi Aniefuna

