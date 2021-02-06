##!/usr/bin/env python
'''
                      ::::::
                    :+:  :+:
                   +:+   +:+
                  +#++:++#++:::::::
                 +#+     +#+     :+:
                #+#      #+#     +:+
               ###       ###+:++#""
                         +#+
                         #+#
                         ###
'''
__author__ = "Alex Pujols"
__copyright__ = "TBD"
__credits__ = ["Alex Pujols"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Alex Pujols"
__email__ = "alex.pujols@gmail.com"
__status__ = "Prototype"

'''
Title	      :	{TBD}
Date		  :	{XX-XX-20XX}
Description   :	{TBD}
Options	      :	{TBD}
Notes	      :	{TBD}
'''

# Import modules declarations
from random import randint
from collections import Counter
#1from memory_profiler import memory_usage
from time import sleep
import timeit
import string
import random

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
# Function to return a random string
def random_string(size):
    temp_string = ' '.join([random.choice(string.ascii_lowercase) for i in range(size)])
    array = temp_string.split()
    return array
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
        if array[i] <= array[0]:
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

# Set global vaiables
_samples_ = 10

while True:
    print ("\n")
    print ("Hi, which sort method would you like to run?")
    print ("1 - Bubble Sort (Integers)")
    print ("2 - Qucksort (Integers)")
    print ("3 - Bubble Sort (Strings)")
    print ("4 - Qucksort (Strings)")
    print ("0 - EXIT")

    # Take user input and validate
    algorithm = input_validate()

    #If user selects integer bubble sort
    if (algorithm == 1):
        print ("\nYou selected bubble sort for integers\n")
        print ("What is the size of the array you wish to create?")
        size = input_validate()
        array = [randint(1, 10000) for i in range(size)]
        print ("\nBEFORE\n", array)
        # To time the execution of the algorithm for analysis
        times = timeit.repeat("bubble_sort(array)", setup="from __main__ import bubble_sort, array", number=_samples_)
        array = bubble_sort(array)
        print ("\nAFTER\n", array)
        print (f"\nThe minimum time to execute across {_samples_} samples was: {format(min(times), '.10f')} seconds!")
    # If user selects integer quicksort
    if (algorithm == 2):
        print ("\nYou selected quicksort for integers \n")
        print ("What is the size of the array you wish to create?")
        size = input_validate()
        array_string = [randint(1, 10000) for i in range(size)]
        print ("\n BEFORE \n", array)
        # To time the execution of the algorithm for analysis
        times = timeit.repeat("quicksort(array)", setup="from __main__ import quicksort, array", number=_samples_)
        array = quicksort(array)
        print ("\n AFTER \n", array)
        print (f"\nThe minimum time to execute across {_samples_} samples was: {format(min(times), '.10f')} seconds!")
    # If user selects string bubblesort
    if (algorithm == 3):
        print ("\nYou selected bubble sort for strings \n")
        print ("What is the size of the array you wish to create?")
        size = input_validate()
        array = random_string(size)
        print ("\n BEFORE \n", array)
        # To time the execution of the algorithm for analysis
        times = timeit.repeat("bubble_sort(array)", setup="from __main__ import bubble_sort, array", number=_samples_)
        array = bubble_sort(array)
        print ("\n AFTER \n", array)
        print (f"\nThe minimum time to execute across {_samples_} samples was: {format(min(times), '.10f')} seconds!")
    # If user selects string quicksort
    if (algorithm == 4):
        print ("\nYou selected quicksort for strings \n")
        print ("What is the size of the array you wish to create?")
        size = input_validate()
        array = random_string(size)
        print ("\n BEFORE \n", array)
        # To time the execution of the algorithm for analysis
        times = timeit.repeat("quicksort(array)", setup="from __main__ import quicksort, array", number=_samples_)
        array = quicksort(array)
        print ("\n AFTER \n", array)
        print (f"\nThe minimum time to execute across {_samples_} samples was: {format(min(times), '.10f')} seconds!")
    #If user selects exit
    if (algorithm == 0):
        print ("\n You have chosen to leave the program.  Goodbye! \n")
        break
