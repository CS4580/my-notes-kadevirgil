"""Fist look at numpy
"""
import numpy as np

def main():
    """Driven function
    """
    # Generate a 1d array with values from 0 to 2
    arr1d = np.array([1, 2, 0, 2, 1, 0, 2, 2, 1, 2])
    print(arr1d, type(arr1d))
    

if __name__ == '__main__':
    main()