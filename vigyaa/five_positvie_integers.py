"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""

"""
solution to this is,

step 1) find the total or sum of the given array

step 2) To find the minimum sum value we need to subtract the maximum value in the array from total/sum 

step 3) To find the maximum sum value we need to subtract the minimum value in the array from the total/sum

step 4) we return the minimum sum value and maximum sum value.          

ex: arr = [1, 3, 5, 7, 9]

we have to use the four integers to get the minimum sum value so the only number we can exclude in the arr is 9 which 
is also the maximum number in the array. so we subtract 25 - 9 = 16
similarly we do for the maximum sum value we find the lowest value in the arr i.e 1 so we subtract 25 - 1 = 24.  

"""

values = [1, 3, 5, 7, 9]


def min_max(list_val):
    total = sum(list_val)
    maximum_sum = total - min(list_val)
    minimum_sum = total - max(list_val)
    return minimum_sum, maximum_sum


print(min_max(values))
