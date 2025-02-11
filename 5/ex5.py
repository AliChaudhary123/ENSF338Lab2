# ENSF 338
#Lab2
# Exercise 5

import timeit
import numpy as np
import matplotlib.pyplot as plt
import scipy


# Linear search:
def linear_search(item, data):
    for i in range(0, len(data)):
        if data[i] == item:
            return i
    return -1
        

# Binary search:
def binary_search(item, data):
    lower = 0
    upper = len(data) - 1

    while lower <= upper:
        mid = lower + (upper - lower) // 2

        if data[mid] == item:
            return mid
        elif data[mid] > item:
            upper = mid - 1
        else:
            lower = mid + 1

    return -1


def log(x, a, b):
    return a * np.log(x) + b
    

# Make the nessecary lists
list_lengths = [1000, 2000, 4000, 8000, 16000, 32000]
avg_linear = []
avg_binary = []

for length in list_lengths:

    # Make a sorted list of length
    sorted = []
    for i in range(0, length):
        sorted.append(i)

    # Pick a random element
    element = np.random.randint(0, length)

    # Time how long it takes for the two searches to find the random element in the array and append average time
    avg_linear.append(timeit.timeit(lambda: linear_search(element, sorted), number=100))
    avg_binary.append(timeit.timeit(lambda: binary_search(element, sorted), number=100))

# Fit linear search line
slope, intercept = np.polyfit(list_lengths, avg_linear, 1)
print()
print("Linear search variables:")
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print()

# Plot unfitted data
plt.scatter(list_lengths, avg_linear)

# Generate y values from fitted line
linevalues = [slope * x + intercept for x in list_lengths]

# Plot fitted line
plt.plot(list_lengths, linevalues, 'r', label="average processing time vs. number of records")

# Fit binary search curve
popt, _ = scipy.optimize.curve_fit(log, list_lengths, avg_binary)
a, b = popt
print("Binary search variables:")
print(f"a: {a}")
print(f"b: {b}")

# Generate y values from fitted curve
fitted_avg_binary = [log(x, a, b) for x in list_lengths]

# Plot unfitted data
plt.scatter(list_lengths, avg_binary)
# Plot fitted curve
plt.plot(list_lengths, fitted_avg_binary, 'r', label="average processing time vs. number of records")

plt.show()

# Question 4 answer:
# For linear search the interpolating function was a line in the form mx + b, where m is the slope and b is the y intercept.
# For binary search the interpolating funciton wan a logarthmic function in the form a(log base e of x) + b.
# The actual values for the variables are printed each time the program is run.
# The results are as expected because linear search has an average case time complexity of O(n) as it goes thorugh all elements
# in an array until it finds what it's looking for, and binary search has an average case time complextiy of O(logn) since 
# it divides the array in two every iteration until it finds the desried element
