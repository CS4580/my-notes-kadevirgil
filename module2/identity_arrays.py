""" array identities with numpy
"""

import numpy as np


def main():
    """Driven function"""
    # Create a 2d 3x3 array of uints
    id_matrix = np.eye(3, 5)
    print(id_matrix)

    diag_matrix = np.diag([2, 3, 4, 5])
    print(diag_matrix)

    # Create a 5x3 matrix of units filled with 0s
    uint_matrix = np.zeros((5, 3), dtype=np.uint)
    print(f"\nuint_matrix: \n{uint_matrix}")

    # Create a 5x3 matrix of units filled with 1s
    uint_matrix2 = np.ones((5, 3), dtype=np.uint)
    print(f"\nuint_matrix2: \n{uint_matrix2}")

    # Create a 5x3 matrix of units filled with pi
    pi_matrix = np.full((5, 3), np.pi)
    print(f"\nfull matrix: \n{pi_matrix}")

    # Create a 5x3 matrix of units filled with random values
    rand_matrix = np.random.random((5, 3))
    print(f"\nrandom matrix: \n{rand_matrix}")


if __name__ == "__main__":
    main()
