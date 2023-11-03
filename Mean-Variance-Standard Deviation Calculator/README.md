# Mean-Variance-Standard Deviation Calculator

## Overview

Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

The returned dictionary should follow this format:

{ <br />
  'mean': [axis1, axis2, flattened],<br />
  'variance': [axis1, axis2, flattened],<br />
  'standard deviation': [axis1, axis2, flattened], <br />
  'max': [axis1, axis2, flattened], <br />
  'min': [axis1, axis2, flattened], <br />
  'sum': [axis1, axis2, flattened] <br />
}

If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

For example, calculate([0,1,2,3,4,5,6,7,8]) should return:

{ <br />
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], <br />
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], <br />
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611], <br />
  'max': [[6, 7, 8], [2, 5, 8], 8], <br />
  'min': [[0, 1, 2], [0, 3, 6], 0], <br />
  'sum': [[9, 12, 15], [3, 12, 21], 36] <br />
}

The unit tests for this project are in test_module.py.
