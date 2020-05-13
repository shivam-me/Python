'''
Smallest Difference

#### Problem Statement


Write a function that takes in two non-empty arrays of integers. The function should nd the pair of numbers(one from the rst array, one from the second array)
whose absolute difference is closest to zero. The function should return an array containing these two numbers, with the number from the rst array in the rst
position. Assume that there will only be one pair of numbers with the smallest difference.
Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
Sample output: [28, 26]


#### Explanation

To traverse in array use left and right pointer to traverse

We can use a Stack here
'''

# O(nlog(n) + mlon(m)) time | O(1) space takes 0.133 seconds
def smallestDifference(arrayOne, arrayTwo):
	array_one = sorted(arrayOne)
	array_two = sorted(arrayTwo)
	index_one = 0
	index_two = 0
	smallestDiff = float("inf")  # Used for big initialisation
	result_pair = []
	while index_one < len(array_one) and index_two < len(array_two):
		first_num = array_one[index_one]
		second_num = array_two[index_two]
		currentDiff = abs(first_num - second_num)
		if currentDiff < smallestDiff:
			smallestDiff = currentDiff
			result_pair = [first_num, second_num]
		if first_num <= second_num:
			index_one += 1
		else:
			index_two += 1

	return result_pair

# My Solution O(n^2) Takes 0.127 seconds
def small(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    diff = float("inf")
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if(abs(arr1[i]-arr2[j]) < diff):
                diff = abs(arr1[i]-arr2[j])
                m, n = i, j

    return [arr1[m], arr2[n]]

array_one = [-1, 5, 10, 20,24,31,54,45,6,43,44,245,67,88,43,56, 28, 3]
array_two = [26, 134, 135, 15, 17]
print(smallestDifference(array_one, array_two))


