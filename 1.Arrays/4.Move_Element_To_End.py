'''
# Move_Element_To_End

## Problem Statement

You are given an array of integers and an integer.Write a function that moves all instances of the integer in the array to the end
of the array and returns the array.
The function should perform this in place(i.e it should mutate the input array ) and dosen't need to maintain the order of the other
integers

Sample Input : array[2,1,2,2,2,3,4,2]
			   toMove =2
Sample Output : [1,3,4,2,2,2,2,2] # 1,3,4 can be ordered differently

'''
# My Solution



# Original Solution
def moveElementToEnd(array, toMove):
	left=0
	right=len(array)-1
	while left < right:
		if array[right] == toMove: # If integer already present in right then shift the right pointer to left by 1
			right -= 1
		if array[left] != toMove:  # If integer is not present in left then shift the left pointer to right by 1
			left += 1
		if array[left] == toMove and array[right] != toMove: # If integer is present in left and not in right,then swap
			array[left], array[right] = array[right], array[left]
	return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
