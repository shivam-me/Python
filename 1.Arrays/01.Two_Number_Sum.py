'''
Two Number Sum

#### Problem Statement

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order.
If no two numbers sum up to the target sum, the function should return an empty array.
Assume that there will be at most one pair of numbers summing up to the target sum.

`Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
Sample output: [-1, 11]


#### Explanation

We can use a Stack here


'''

# Solution 1
# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    result_list = [] # Target Array
    for i in range(0, len(array) - 1):
        first_number = array[i]  # Store First Value i.e 3
        for j in range(i + 1, len(array)): # For comparing first(3) with other numbers 5,-1,-4,8,11,1,-1,10 and so on
            second_number = array[j] # Store Second Value j=(i+1)
            sum = first_number + second_number # Find sum
            if sum == targetSum: # Check if sum is equal to target or not
                result_list.append(first_number)
                result_list.append(second_number)

    return sorted(result_list)
# Solution 1 ends

# Solution 2 starts
# O(n) time | O(n) space
def twoNumberSum2(array, targetSum):
    result_list = []
    for i in range(0, len(array) - 1):
        first_number = array[i]
        second_nsumber_expected = targetSum - first_number
        secondary_array = array[i + 1:len(array)] # Secondary array becomes array without first number
        # print(secondary_array)
        # [3, -4, 8, 11, 1, -1, 6] when first_number = 5
        # [-4, 8, 11, 1, -1, 6] when first_number = 3
        # [8, 11, 1, -1, 6] when first_number = -4
        # [11, 1, -1, 6] when first_number = 8
        # [1, -1, 6] when first_number = 11
        # [-1, 6] when first_number = 1
        # [6] when first_number = -1
        if second_nsumber_expected in secondary_array:
            result_list.append(first_number)
            result_list.append(second_nsumber_expected)

    return sorted(result_list)
# Solution 2 ends

# Solution 3 starts
# O(nlogn) time | O(1) space
def twoNumberSum3(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:  # Left and right are indices
        current_sum = array[left] + array[right]
        if current_sum == targetSum:
            return [array[left], array[right]]  # Return Final list when condition is true
        elif current_sum < targetSum:
            left += 1
        elif current_sum > targetSum:
            right -= 1

    return []
# Solution 3 ends

print(twoNumberSum([5, 3, -4, 8, 11, 1, -1, 6], 10))
