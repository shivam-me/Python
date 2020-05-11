'''
Three Number Sum

#### Problem Statement


Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should nd all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets.
The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with
respect to the numbers they hold. If no three numbers sum up to the target sum, the function should return an empty array.

Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0

Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]


#### Explanation

We can use a Stack here

'''
# O(n^2) time | O(n) space
def three_number_sum(array, targetSum):
    array.sort()
    triplates = []
    for i in range(len(array) - 2):
        left_index = i + 1
        right_index = len(array) - 1
        while left_index < right_index:
            sum = array[i] + array[left_index] + array[right_index]
            if sum == targetSum:
                triplates.append(array[i])
                triplates.append(array[left_index])
                triplates.append(array[right_index])
                left_index += 1
                right_index -= 1
            elif sum < targetSum:
                left_index += 1
            elif sum > targetSum:
                right_index -= 1
    return triplates


sample_input_array = [12, 3, 1, 2, -6, 5, -8, 6]
sample_sum = 0
result = three_number_sum(sample_input_array, sample_sum)
print("The sets of triplates are: ", result)
