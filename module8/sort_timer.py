# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 08/07/2023
# Description: Calculated running time

from time import perf_counter
from random import randint
from functools import wraps
from matplotlib import pyplot

def sort_timer(func):
    """
    Create a timing decorator sort_timer
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()      # uses perf_counter to record the start and end times of the decorated function
        result = func(*args, **kwargs)
        end = perf_counter()
        return end - start      # uses perf_counter to record the start and end times of the decorated function
    return wrapper

@sort_timer
def bubble_sort(a_list):    
  """    
  Sorts a_list in ascending order    
  """    
  for pass_num in range(len(a_list) - 1):        
    for index in range(len(a_list) - 1 - pass_num):            
      if a_list[index] > a_list[index + 1]:                
        temp = a_list[index]                
        a_list[index] = a_list[index + 1]                
        a_list[index + 1] = temp

@sort_timer  
def insertion_sort(a_list):    
  """    
  Sorts a_list in ascending order    
  """    
  for index in range(1, len(a_list)):        
    value = a_list[index]        
    pos = index - 1        
    while pos >= 0 and a_list[pos] > value:            
      a_list[pos + 1] = a_list[pos]            
      pos -= 1        
    a_list[pos + 1] = value

def make_lists_of_sort_times(sort1, sort2, lengths):
    """
    Create the function make_lists_of_sort_times
    """
    times1 = []
    times2 = []
    for n in lengths:
        lst = [randint(1,10000) for i in range(n)]
        lst2 = list(lst)            # the function make_lists_of_sort_times
        times1.append(sort1(lst))
        times2.append(sort2(lst2))
    return times1, times2       # sort the copied list with two sorting functions respectively, and record the sorting time
    
def compare_sorts(sort1, sort2):
    """
    Create the compare_sorts function to compare the time of the two sorting algorithms
    """
    lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    times1, times2 = make_lists_of_sort_times(sort1, sort2, lengths)        # plot a comparison chart
    pyplot.plot(lengths, times1, 'ro--', linewidth=2, label='Bubble Sort')
    pyplot.plot(lengths, times2, 'go--', linewidth=2, label='Insertion Sort')
    pyplot.xlabel("Size of List Being Sorted")
    pyplot.ylabel("Seconds to sort")
    pyplot.legend()
    pyplot.show()

compare_sorts(bubble_sort, insertion_sort)
