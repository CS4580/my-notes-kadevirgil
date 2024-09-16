""" Range Arrays using range()
"""

import numpy as np


def main():
    """Driven function"""
    arr = np.arange(-4, 19)
    print(arr, arr.dtype)

    # Generate an array with values from 0 to 5 in steaps of 0.1
    arr = np.arange(0, 5, 0.1)
    print(arr, arr.dtype)

    # Ranges with decimal values
    arr = np.arange(0.1, 0.8, 0.01)
    print(arr, arr.dtype)


if __name__ == "__main__":
    main()
