'''

Largest Range

#### Problem Statement

Write a function that takes in an array of integers and returns an array of length 2 representing the largest
range of numbers contained in that array. The first number in the output array should be the first number in
the range while the second number should be the last number in the range. A range of numbers is as a set of
numbers that come right after each other in the set of real integers. For instance, the output array [2, 6]
represents the range {2, 3, 4, 5, 6}, which is a range of length 5. Note that numbers do not need to be
ordered or adjacent in the array in order to form a range. Assume that there will only be one largest range.


Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Sample output: [0, 7]


#### Solution
'''

# O(n) time | O(n) space
def largestRange(array):
    bestRange = []
    longestLength = 0
    nums = {}
    for num in array: # Mark each numbers as true in our hash table
        nums[num] = True
    for num in array:
        if not nums[num]: # If a number is not true i.e false in hash table we will continue and skip that number
            continue # Helps if the value is already false ,we don't have to iterate again to below loops
        # After Third iteration with num = 15 ,directly goto line 48 and evaluates false and dosen't return
        nums[num] = False
        currentLenght = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False # Falsify value in order 1,0 then shift to below loop beacuse -1 don't exist in table
            currentLenght += 1
            left -= 1
        while right in nums:
            nums[right] = False # Falsify value in order 2,3,4,5,6,7 then goto below if condition
            currentLenght += 1
            right += 1
            # Currentlength = 8 after above 2 loops in first iteration [0 to 7]
            # Currentlength = 3 after above 2 loops in second iteration [10 to 12]
            # Currentlength = 1 after above 2 loops in third iteration [15]
        if currentLenght > longestLength:
            longestLength = currentLenght
            bestRange = [left + 1, right - 1] # Because we included extras in above loops so we need to remove them beacuse of 40 and 44

    return bestRange # Returns [0,7] in first iteration ,second and third iteration don't get the chance


print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
