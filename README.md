# The Rainfall Problem

(C) James Grant (r.j.grant@bath.ac.uk)

The repository contains exercises based around the classic rainfall problem, to design a function which:

1. Given a list of 'rainfalls' find the mean rainfall
2. Negative values should be ignored 
3. If the value `99` is encoutered, the average is calculated on values up to but not including `99`

The repository consists of a set of tests `test_*.py` and prototype functions `rainfall.py`.  The students aim to write functions to satisfy the tests.

Continuations of the exercise generalise to user defined `STOP` value and correct and add new test in `test_enhanced.py`.

[![Azure Notebooks](https://notebooks.azure.com/launch.png)](https://notebooks.azure.com/import/gh/<GitHub_username>/<repository_name>)

# Future

Developments of the exercise could read in values from a datafile, and extend the mean to calculate standard deviation, concurrently and separately.

More detailed instructions about this exercise are available in the [Now Code lesson](https://arc-bath.github.io/now-code/01-rainfall.html).
