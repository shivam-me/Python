'''
Four Number Sum

#### Problem Statement

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should nd all quadruplets in the array that sum up to the target sum and return a two-dimensional
array of all these quadruplets in no particular order. If no four numbers sum up to the target sum, the function
should return an empty array.


Sample input: [7, 6, 4, -1, 1, 2], 16
Sample output: [[7, 6, 4, -1], [7, 6, 1, 2]]


#### Solution

'''
#   Average:    O(n^2) time  | O(n^2) space
#   Worst:      O(n^3) time  | O(n^2) space
def fourNumberSum(array, targetSum):
    allPairSums = {}  # For hash map
    quadruplets = []
    # As we can skip first and last values as it wont add to hashmap or simply for i in range(0, len(array)):
    for i in range(1, len(array) - 1):
        for j in  range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]]) # Pair is array stored in hashmap
        for k in range(0, i): # For adding pairs to hashmap this should be always done after the above loop
            currentSum = array[i] +  array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quadruplets



input = [7,  6, 4, -1, 1, 2]
output = fourNumberSum(input, 16)
print('Quadruplets: ', output)





# From Leetcode.com solution all are trash
# https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
# https://leetcode.com/problems/4sum/discuss/8759/A-conise-python-solution-based-on-ksum

# Uses 2 number sum to find K sum
def fourSum(self, nums, target):
    def findNsum(l, r, target, N, result, results):
        if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:  # reduce to N-1 sum problem
            for i in range(l, r+1):
                if i == l or (i > l and nums[i-1] != nums[i]):
                    findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

    nums.sort()
    results = []
    findNsum(0, len(nums)-1, target, 4, [], results)
    return results


# Uses 3 number sum to find K sum
class Solution(object):
  def threeSum(self, nums, target):
    results = []
    nums.sort()
    for i in range(len(nums)-2):
      l = i + 1; r = len(nums) - 1
      t = target - nums[i]
      if i == 0 or nums[i] != nums[i-1]:
        while l < r:
          s = nums[l] + nums[r]
          if s == t:
            results.append([nums[i], nums[l], nums[r]])
            while l < r and nums[l] == nums[l+1]: l += 1
            while l < r and nums[r] == nums[r-1]: r -= 1
            l += 1; r -=1
          elif s < t:
            l += 1
          else:
            r -= 1

    return results

  def fourSum(self, nums, target):
    results = []
    nums.sort()
    for i in range(len(nums)-3):
      if i == 0 or nums[i] != nums[i-1]:
        threeResult = self.threeSum(nums[i+1:], target-nums[i])
        for item in threeResult:
          results.append([nums[i]] + item)
    return results

# NOTE:
# Complexity of 2-sum is O(N), 3-sum is O(N^2), 4-sum would be O(N^3)....in general is complexity of k-sum O(N^k-1)?


