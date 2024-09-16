""" Array indexing practice
"""

import numpy as np


def main():
    """Driven function"""
    arr1d = np.arange(10)
    # Access th second element
    print(arr1d[1], arr1d[1].dtype)

    # Negative indexing
    print(arr1d[-1], arr1d[-1].dtype)

    # 2d array indexing using [n, m]
    arr2d = np.array([[21, 44, 55], [66, 45, 65], [12, 91, 292]])
    print(arr2d[0, 0])
    print(arr2d[2, -2])  # Negative indexing is also supported
    print(arr2d[0])  # Print a whole row

    # Slicing
    arr1d = np.arange(10)
    print(f"Slicing elements 1:4:2 {arr1d[1:4]}")  # Splice the array from index 1 to 4
    print(f"Reverse the array {arr1d[::-1]}")  # Reverse the array
    print(
        f"Slicing elements 1:4:2 {arr1d[1:4:2]}"
    )  # The third parameter defines the steps

if __name__ == "__main__":
    main()
