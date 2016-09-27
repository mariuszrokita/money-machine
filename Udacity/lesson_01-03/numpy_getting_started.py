"""Creating NumPy arrays."""

import numpy as np


def print_array(title, array):
    print(title, ":")
    print(array)
    print("")


def test_run():
    # List to 1D array
    print_array("1D array", np.array([2, 3, 4]))

    # List to tuples to 2D array
    print_array("tuples to 2D array", np.array([(2, 3, 4), (5, 6, 7)]))

    # Empty array
    print_array("empty array", np.empty(5))

    # Empty 2D array
    print_array("empty array with 5 rows and 4 columns", np.empty((5, 4)))

    # Array full of 1s
    print_array("array full of 1s", np.ones((5, 4)))

    # Array full of 1s specified as integers
    print_array("array full of 1s", np.ones((5, 4), dtype=np.int_))

if __name__ == "__main__":
    test_run()
