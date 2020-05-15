'''

Subarray Sort

#### Problem Statement

Write a function that takes in an array of integers of length at least 2. The function should return an array
of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place
in order for the entire input array to be sorted. If the input array is already sorted, the function should
return [-1, -1].

Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Sample output: [3, 9]


#### Solution

'''
import math

def subarraySort(array):
    minOutOfOrder = math.inf  # float("inf")
    maxOutOfOrder = -math.inf  # float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array): # Check for Number which is not in sorted form
            minOutOfOrder = min(minOutOfOrder, num)  # Find the minimum number among unsorted numbers
            maxOutOfOrder = max(maxOutOfOrder, num)  # Find the maximum number among unsorted numbers
            # After i=5(11) min = 11 and max = 11  as 7< 11 not in sorted form
            # After i=6(7) min = 7 and max = 11
            # After i=7(12) min = 7 and max = 12
            # After i=8(6) min = 6 and max = 12
            # After i=9 to 12 min = 6 and max = 12

    if minOutOfOrder == math.inf: # or maxOutOfOrder == -math.inf which means if numbers are sorted already
        return [-1, -1]

    subArrayLeftIdx = 0
    while array[subArrayLeftIdx] <= minOutOfOrder: # Check position where min number can be placed i.e find index
        subArrayLeftIdx += 1 # If not found increment left pointer
        # subArrayLeftIdx will go 0,1,2,3 then stop with final value = 3

    subArrayRightIdx = len(array) - 1
    while maxOutOfOrder <= array[subArrayRightIdx]: # Check position where max number can be placed
        subArrayRightIdx -= 1  # If not found decrement right pointer
        # subArrayRightIdx will go 12,11,10,9 then stop with final value = 9
    return [subArrayLeftIdx, subArrayRightIdx] # returns 3 and 9


def isOutOfOrder(i, num, array):
    if i == 0: # For first number, num will be greater than its next number
        return num > array[i + 1] # Because there is nothing to its left
    if i == len(array) - 1:  # For last number, num will be lesser than second last number
        return num < array[i - 1]  # Because there is nothing to its right
    return num < array[i - 1] or num > array[i + 1]


print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
