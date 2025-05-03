import numpy as np
import numpy.typing as npt
from scipy.stats import zscore


Timeseries = npt.NDArray[np.float64]


def moving_average(data: Timeseries, window_size=5) -> Timeseries:
    """
    Moving average, or alternatively a low pass filter for Timeseries data
    :param data: a time series
    :param window_size: averaging window size
    :return: Averaged timeseries
    """
    y_smooth = np.convolve(data[:, 1], np.ones(window_size) / window_size, mode='valid')
    x_smooth = data[:, 0][:len(y_smooth)]
    return np.column_stack((x_smooth, y_smooth))



def filter_outliers(data: Timeseries, zscore_upper_limit = 2):
    """
    Remove values with a z score higher than zscore_upper_limit
    Mean and Variance are calculated on the input timeseries
    :param zscore_upper_limit: limit above which the sample is discarded
    :param data: a time series
    :return: A filtered timeseries, with outliers removed
    """
    z_scores = zscore(data[:, 1])
    mask = np.abs(z_scores) < zscore_upper_limit
    return data[mask]