import timeit
import matplotlib.pyplot as plt
import numpy as np
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
    '''
    QUESTION 1: What does this code do?
    Answer: 
    This code follows the rules of the fibonacci sequence. This is a recursive function because it calls the function func twice to return its value. 
    It takes an integer value n to describe the iteration in the sequence. If the n value is 0 or 1, the value returned will be the values of 0 and 1 respectively. 
    However, as we progress through the sequebce, the function uses recursion to add the previous 2 values.

    QUESTION 2: Is this an example of a divide-and-conquer algorithm?
    Answer:
    This code is not an example of divide-and-conquer. Divide and Conquer uses recursion, but not vice versa.
    This is because divide-and-conquer requires the main problem to be broken down into subparts and solved recursively. 

    QUESTION 3: What is the time complexity?
    Answer: O(2^n) (exponential). Each call generates twice more calls every time it is called. Makes it much slower.
    '''
    #Question 4: Memoization
def mem_func(n, cache = {}): #Dictionary
    if n == 0 or n == 1:
        return n
    if n not in cache:
        cache[n] = mem_func(n-1, cache) + mem_func(n-2, cache)
    return cache[n]
    #Question 5: Time Complexity -> O(n) (linear). Each fibonacci is calculated once and then is stored, which removes the need for extra calculations. 

    #Question6
def timed():
    original = []
    mem = []

    for n in range(36):
        original_time = timeit.timeit(lambda: func(n), number = 1)
        original.append(original_time)
        print(f"The time for the original is: {original_time} seconds" )

        mem_time = timeit.timeit(lambda: mem_func(n), number = 1)
        mem.append(mem_time)
        print(f"The time for the memoized is: {mem_time} seconds" )

    return original, mem
    
def graph(original, mem):

    n_values = list(range(36))

    plt.plot(n_values, original, label = "Original", color = 'b')
    plt.xlabel("n")
    plt.ylabel("Time(seconds)")
    plt.title("Original")
    plt.savefig("ex1.6.1.jpg")
    plt.show()

    plt.figure()
    plt.plot(n_values, mem, label = "Memoized", color = 'r')
    plt.xlabel("n")
    plt.ylabel("Time(seconds)")
    plt.title("Memoized Recursion")
    plt.ylim(0e-5, 8.25e-4)
    plt.savefig("ex1.6.2.jpg")
    plt.show()
    





def main():
    original, mem = timed()
    graph(original, mem)

        

if __name__ == '__main__':
    main()

        
