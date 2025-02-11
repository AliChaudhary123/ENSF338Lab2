import timeit
import pstats
import cProfile

def sub_function(n):
#sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]


test_function()
third_function()

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    test_function()
    third_function()

    profiler.disable()
    
    # Print profiling stats
    stats = pstats.Stats(profiler)
    stats.sort_stats(pstats.SortKey.TIME)  # Sort by execution time
    stats.print_stats(10)  # Show top 10 function calls


'''
1. A profiler is a function that describes how long various different parts of the program
will take to execute; a set of statistics represents this information, and it can very useful to understand
where exactly your program may be spending the most time or expending the most resources. 

    
2. This is in contrast to benchmarks which analyse the overall performance of the program, not specific sections
    and metrics as a profiler would. This is better for comparison and tracking a programs efficiently over time or with other 
    programs. 

4. Samle Output: [Running] python -u "/Users/aliawan/Desktop/ENSF338_Notebook/Lab2/ex3.py"
         68 function calls (23 primitive calls) in 3.621 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    3.621    3.621    3.621    3.621 /Users/aliawan/Desktop/ENSF338_Notebook/Lab2/ex3.py:18(third_function)
        1    0.000    0.000    0.000    0.000 /Users/aliawan/Desktop/ENSF338_Notebook/Lab2/ex3.py:12(test_function)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
    55/10    0.000    0.000    0.000    0.000 /Users/aliawan/Desktop/ENSF338_Notebook/Lab2/ex3.py:5(sub_function)

    

    As we can see in this sample output, all of the execution time is being spent on the "third function" function.

'''
