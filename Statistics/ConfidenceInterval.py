from statistics import mean
from Statistics.StandardDeviation import StdDevSample
from Statistics.Zscore import Z_scores


from Statistics.Zscore import z_values


def mean_confidence_interval(data):
    n = len(data)
    List = []
    std = StdDevSample(data)
    mu = mean(data)
    z_list = Z_scores(z_values(data))
    SE = std / n
    for i in z_list:
        left = mu - i * SE
        right = mu + i * SE
        List.append([left, right])
    return List