##!/usr/bin/env python
__author__ = "Alex Pujols"
__copyright__ = "Copyright 2021, Evaluating Sorting Algorithms Project TIM-6110 wk5"
__credits__ = ["Alex Pujols"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Alex Pujols"
__email__ = "alex.pujols@gmail.com"
__status__ = "Prototype"
# Import modules declarations
from random import randint
from collections import Counter
from memory_profiler import memory_usage
from time import sleep
import timeit

# Function declarations

# Function to test for valid input and convert to int for further processing
def input_validate():
    while True:
        try:
            validate = int(input(": "))
            break
        except:
            print ("Incorrect value! Please make a new selection")
    return validate
# Function to perform bubble sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        # Is this already sorted? If so, move on
        already_sorted = True
        # Start the sort
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        # If there are no more sorts we are done
        if already_sorted:
            break
    return array
# Function to perfom quicksort
def quicksort(array):
    n = len(array)
    # Should we continue
    if n < 2:
        return array
    # Establish current placement
    pivot = 0
    # Begin sorting values into temporary arrays
    for i in range(1, n):
        if array[i] <= array [0]:
            pivot += 1
            temp = array[i]
            array[i] = array[pivot]
            array[pivot] = temp
    # Reset where appropriate prior to recursive calls
    temp = array[0]
    array[0] = array[pivot]
    array[pivot] = temp
    # Make recursive calls to call left and right sorts
    left = quicksort(array[0:pivot])
    right = quicksort(array[pivot+1:n])
    # Assemble sorted array and return back to main function
    array = left + [array[pivot]] + right
    return array

# Main code begins

# Set globals

while True:
    print ("\n\n")
    print ("Hi, which sort method would you like to run?")
    print ("1 - Bubble Sort (Integers)")
    print ("2 - Qucksort (Integers)")
    print ("3 - Bubble Sort (Strings)")
    print ("4 - Qucksort (Strings)")
    print ("0 - EXIT")

    # Take user input and validate
    algorithm = input_validate()

    #If user selects spacial analysis
    if (selection == 1):
        print ("\n You selected bubble sort for integers\n")
        print ("What is the size of the array you wish to create?")
        size = input_validate()
        array = [randint(1, 10000) for i in range(size)]
        print ("\n AFTER \n", array)
        times = timeit.repeat("bubble_sort(array)", setup="from __main__ import bubble_sort, array", number=samples)
        print ("\n AFTER \n", array)
        print ("\n The minimum time to execute across ", samples, " samples was: ", min(times))
    # If user selects insertion sort
    if (algorithm == 2):
        print ("\n You selected quicksort for integers \n")
        print ("What is the size of the array you wish to create?")
        size = input_validate()
        array = [randint(1, 10000) for i in range(size)]
        print ("\n AFTER \n", array)
        times = timeit.repeat("quicksort(array)", setup="from __main__ import quicksort, array", number=samples)
        print ("\n AFTER \n", array)
        print ("\n The minimum time to execute across ", samples, " samples was: ", min(times))
    # If user selects quicksort
    if (algorithm == 3):
        print ("\n You selected bubble sort for strings \n")
        print ("What is the size of the array you wish to create?")
        size = input_validate()
        array = [randint(1, 10000) for i in range(size)]
        print ("\n BEFORE \n", array)
        times = timeit.repeat("bubble_sort(array)", setup="from __main__ import bubble_sort, array", number=samples)
        print ("\n AFTER \n", array)
        print ("\n The minimum time to execute across ", samples, " samples was: ", min(times))
    if (algorithm == 4):
        print ("\n You selected quicksort for strings \n")
        print ("What is the size of the array you wish to create?")
        size = input_validate()
        array = [randint(1, 10000) for i in range(size)]
        print ("\n BEFORE \n", array)
        times = timeit.repeat("quicksort(array)", setup="from __main__ import quicksort, array", number=samples)
        print ("\n AFTER \n", array)
        print ("\n The minimum time to execute across ", samples, " samples was: ", min(times))
    #If user selects exit
    if (selection == 0):
        print ("\n You have chosen to leave the program.  Goodbye! \n")
        break
