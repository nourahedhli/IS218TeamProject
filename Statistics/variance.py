from Statistics.standardDeviation import StandardDeviationPopulation
from Statistics.standardDeviation import StandardDeviationSample
from Calculator.squareRoot import squareRoot


def population_variance(data):
    x = StandardDeviationPopulation(data)
    return squareRoot(x)


def sample_variance(data):
    x = StandardDeviationSample(data)
    return squareRoot(x)
