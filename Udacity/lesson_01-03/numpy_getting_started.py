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

    # Array full of random number uniformly sampled from [0.0, 1.0)
    print_array("array with random values", np.random.random((5, 4)))  # pass tuple

    # Array full of random number uniformly sampled from [0.0, 1.0)
    print_array("array with random values", np.random.rand(5, 4))

    # Sample numbers from a Gaussian (normal) distribution
    print_array("Gaussian distribution", np.random.normal(size=(2, 3)))  # "standard normal" (mean = 0, s.d. = 1)

    # Sample numbers from a Gaussian (normal) distribution
    print_array("Gaussian distribution", np.random.normal(50, 10, size=(2, 3)))  # mean = 50, s.d. = 10

    ##############################################

    # Random integers
    print("Random integers:")
    print(np.random.randint(10))    # a single integer in [0, 10)
    print(np.random.randint(0, 10))     # same as above, but explicit
    print(np.random.randint(0, 10, size=5))     # 5 random integers as a 1D array
    print(np.random.randint(0, 10, size=(2, 3)))    # 2x3 array of random integers

    ##############################################

    # Array attributes
    a = np.random.rand(5, 4)
    print(a)
    print(a.shape[0])  # number of rows
    print(a.shape[1])  # number of columns
    print(len(a.shape))     # number of dimensions
    print(a.size)   # number of elements

    ##############################################

    # Operations on arrays

    np.random.seed(693)
    a = np.random.randint(0, 10, size=(5, 4))
    print("Array:\n", a)

    # Sum of all elements
    print("Sum of all elements: ", a.sum())

    # Iterate over rows, to compute sum of each column
    print("Sum of each column:\n", a.sum(axis=0))

    # Iterate over columns, to compute sum of each row
    print("Sum of each column:\n", a.sum(axis=1))

    # Statistics
    print("Minimum of each column:\n", a.min(axis=0))
    print("Maximum of each row:\n", a.max(axis=1))
    print("Mean of all elements:", a.mean())

    ##############################################

    a = np.random.random((5, 4))
    # Slicing
    print(a)
    print(a[:, 0:3:2])  # will select every second column from range [0, 3)

    # Assigning a single value to an entire row
    a[0, :] = 2
    print(a)

    # Assigning a list to a column in an array
    a[:, 3] = [1, 2, 3, 4, 5]
    print(a)
    print("")

    ##############################################

    # Accessing elements using list of indices
    indices = np.array([1, 1, 2, 3])  # we will show rows: 1, 1, 2, 3
    print(a[indices])

    # boolean or "mask" index arrays
    a = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0),
                  (0, 2, 50, 20, 0, 1, 28, 5, 0)])
    print(a)

    mean = a.mean()
    print("mean:", mean)

    # masking
    print("masking")
    print(a[a < mean])  # returns only elements that are less than mean

    a[a < mean] = mean  # set value of mean to all elements that are less than mean
    print(a)

    print(a < mean)  # print array and show if elements are less/greater than mean

    ##############################################
    print("Arithmetic operations")
    a = np.array([(1, 2, 3, 4, 5), (10, 20, 30, 40, 50)])
    print("Original array a:\n", a)

    print("\nMultiply a by 2:\n", 2 * a)
    print("\nDivide a by 2:\n", a / 2)

    b = np.array([(100, 200, 300, 400, 500), (1, 2, 3, 4, 5)])
    print("Original array b:\n", b)

    print("\nAdd a + b:\n", a + b)
    print("\nMultiply a * b:\n", a * b)

if __name__ == "__main__":
    test_run()

