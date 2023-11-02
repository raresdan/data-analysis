import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    calculations = {}

    # transforming the list into a 3x3 matrix
    array = np.array(list)
    matrix = array.reshape(3, 3)

    # calculating the means
    mean_axis0 = matrix.mean(axis=0)
    mean_axis1 = matrix.mean(axis=1)
    matrix_mean = array.mean()

    # transforming the results back into lists
    mean_axis0 = mean_axis0.tolist()
    mean_axis1 = mean_axis1.tolist()

    calculations.update({"mean": [mean_axis0, mean_axis1, matrix_mean]})

    # calculating the variance
    variance_axis0 = matrix.var(axis=0)
    variance_axis1 = matrix.var(axis=1)
    matrix_variance = array.var()

    # transforming the results back into lists
    variance_axis0 = np.ndarray.tolist(variance_axis0)
    variance_axis1 = np.ndarray.tolist(variance_axis1)

    calculations.update(
        {"variance": [variance_axis0, variance_axis1, matrix_variance]})

    # calculating the standard deviation
    std_axis0 = matrix.std(axis=0)
    std_axis1 = matrix.std(axis=1)
    matrix_std = array.std()

    # transforming the results back into lists
    std_axis0 = np.ndarray.tolist(std_axis0)
    std_axis1 = np.ndarray.tolist(std_axis1)

    calculations.update(
        {"standard deviation": [std_axis0, std_axis1, matrix_std]})

    # calculating the max
    max_axis0 = matrix.max(axis=0)
    max_axis1 = matrix.max(axis=1)
    matrix_max = array.max()

    # transforming the results back into lists
    max_axis0 = np.ndarray.tolist(max_axis0)
    max_axis1 = np.ndarray.tolist(max_axis1)

    calculations.update({"max": [max_axis0, max_axis1, matrix_max]})

    # calculating the min
    min_axis0 = matrix.min(axis=0)
    min_axis1 = matrix.min(axis=1)
    matrix_min = array.min()

    # transforming the results back into lists
    min_axis0 = np.ndarray.tolist(min_axis0)
    min_axis1 = np.ndarray.tolist(min_axis1)

    calculations.update({"min": [min_axis0, min_axis1, matrix_min]})

    # calculating the sum
    sum_axis0 = matrix.sum(axis=0)
    sum_axis1 = matrix.sum(axis=1)
    matrix_sum = array.sum()

    # transforming the results back into lists
    sum_axis0 = np.ndarray.tolist(sum_axis0)
    sum_axis1 = np.ndarray.tolist(sum_axis1)

    calculations.update({"sum": [sum_axis0, sum_axis1, matrix_sum]})
    return calculations
