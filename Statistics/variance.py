from Statistics.StandardDeviation import StdDevPop
from Statistics.StandardDeviation import StdDevSample
from Calculator.SquareRoot import squareRoot


def population_variance(data):
    x = StdDevPop(data)
    return squareRoot(x)


def sample_variance(data):
    x = StdDevSample(data)
    return squareRoot(x)
