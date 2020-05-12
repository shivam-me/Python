'''
Monotonic_Array

#### Problem Statement

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
An array is said to be monotonic if its elements,from left to right, are entirely non-increasing or entirely non-decreasing.

Sample Input : [-1,-5,-10,-1100,-1100,-1101,-1102,-9001] # if prevN <= currN <= nextN or prevN >= currN >= nextN

Sample Output : true

'''

# Method 1

def isMonotonicNew(array):
    if len(array) <= 2:
        return True
    for i in range(len(array) - 2):
        prevN = array[i]
        currN = array[i+1]
        nextN = array[i+2]
        print(prevN, currN, nextN)
        if prevN <= currN <= nextN or prevN >= currN >= nextN:
            continue
        else:
            return False
    return True

# Method 2 ,just changing the position of pointer

def isMonotonic(array):
    if len(array) <= 2:
        return True
    for i in range(1, len(array) - 1):
        prevN = array[i - 1]
        currN = array[i]
        nextN = array[i + 1]
        # Prints prevN,currN, nextN as
        #  -1    -5     -10
        #  -5    -10    -1100
        #  -10   -1100  -1100
        # -1100  -1100  -1101
        # -1100  -1101  -1102
        # -1101  -1102  -9001
        if prevN <= currN <= nextN or prevN >= currN >= nextN:
            continue
        else:
            return False
    return True


print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))

