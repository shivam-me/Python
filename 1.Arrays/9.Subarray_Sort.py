'''

Subarray Sort

#### Problem Statement

Write a function that takes in an array of integers of length at least 2. The function should return an array of the starting and ending indices of the smallest
subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted. If the input array is already sorted, the function should
return [-1, -1].

Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Sample output: [3, 9]


#### Solution

'''
import math

def subarraySort(array):
    minOutOfOrder = math.inf
    maxOutOfOrder = -math.inf
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    if minOutOfOrder == math.inf:
        return [-1, -1]
    subArrayLeftIdx = 0
    while array[subArrayLeftIdx] <= minOutOfOrder:
        subArrayLeftIdx += 1
    subArrayRightIdx = len(array) - 1
    while maxOutOfOrder <= array[subArrayRightIdx]:
        subArrayRightIdx -= 1
    return [subArrayLeftIdx, subArrayRightIdx]


def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num < array[i - 1] or num > array[i + 1]
