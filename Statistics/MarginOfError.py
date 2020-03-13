from Statistics.Zscore import *
from Statistics.StandardDeviation import *
from Calculator.SquareRoot import squareRoot


def MarginError(data):
    List = []
    SE = (StdDevSample(data) / (squareRoot(len(data))))
    for i in Z_scores(z_values(data)):
        ME = i * SE
        List.append(ME)

    return List
