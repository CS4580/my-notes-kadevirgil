""" 1d arrays
"""

import numpy as np


def main():
    """Driven function"""
    numbers = [-1, -4, 0, 4, 5]

    # Create numpy array
    matrix = np.array([[1, 3, 4], [5, 6, 7]])
    print(matrix, type(matrix))

    # Type specification in numpy
    # Use the dtype optional argument to specify data type
    new_arr = np.array(numbers, dtype=np.short)
    print(new_arr, new_arr.dtype)

    # unsinged data
    pos_numbers = [1, 4, 0, 4, 5]
    new_arr = np.array(pos_numbers, dtype=np.ushort)
    print(new_arr, new_arr.dtype)

    # floats
    fl_numbers = [1.4, 3.5, 6.6, 8.5]
    new_arr = np.array(fl_numbers, dtype=np.float32)
    print(new_arr, new_arr.dtype)


if __name__ == "__main__":
    main()
