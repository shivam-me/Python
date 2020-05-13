'''

Largest Range

#### Problem Statement

Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of numbers contained in that array. The rst
number in the output array should be the rst number in the range while the second number should be the last number in the range. A range of numbers is dened
as a set of numbers that come right after each other in the set of real integers. For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a
range of length 5. Note that numbers do not need to be ordered or adjacent in the array in order to form a range. Assume that there will only be one largest range.


Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Sample output: [0, 7]


#### Solution
'''

# O(n) time | O(n) space
def largestRange(array):
    bestRange = []
    longestLength = 0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currentLenght = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentLenght += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLenght += 1
            right += 1
        if currentLenght > longestLength:
            longestLength = currentLenght
            bestRange = [left + 1, right - 1]
    return bestRange
