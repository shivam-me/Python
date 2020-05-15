'''
 Min Rewards

#### Problem Statement

Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student scores on the nal exam in a particular order (not necessarily
sorted), and you want to reward your students. You decide to do so fairly by giving them arbitrary rewards following two rules: rst, all students must receive at
least one reward; second, any given student must receive strictly more rewards than an adjacent student (a student immediately to the left or to the right) with a
lower score and must receive strictly fewer rewards than an adjacent student with a higher score. Assume that all students have different scores; in other words,
the scores are all unique. Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to students, all the
while satisfying the two rules.


`Sample input: [8, 4, 2, 1, 3, 6, 7, 9, 5]
Sample output: 25 ([4, 3, 2, 1, 2, 3, 4, 5, 1])`


#### Solution
'''


# Solution #1
# O(n^2) time | O(n) space
def minRewards(score):
    rewards = [1 for _ in score]
    for i in range(1, len(score)):
        j = i - 1
        if score[i] > score[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >=0 and score[j] > score[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1
    return sum(rewards)



# Solution #2
# O(n) time | O(n) space
def minRewards(scores):
    rewards = [1 for _ in scores]
    localMinIdxs = getLocalMinIdxs(scores)
    for localMinIdx in localMinIdxs:
        expandFromLocalMinIdx(localMinIdx, scores, rewards)
    return sum(rewards)


def getLocalMinIdxs(array):
    if len(array) == 1:
        return [0]
    localMinIdxs = []
    for i in range(len(array)):
        if i == 0  and array[i] < array[i + 1]:
            localMinIdxs.append(i)
        if i == len(array) - 1 and array[i] < array[i - 1]:
            localMinIdxs.append(i)
        if i == 0 or  i == len(array) - 1:
            continue
        if array[i] < array[i + 1] and array[i] < array[i - 1]:
            localMinIdxs.append(i)
    return localMinIdxs


def expandFromLocalMinIdx(localMinIdx, scores, rewards):
    leftIdx = localMinIdx - 1
    while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
        rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
        leftIdx -= 1
    rightIdx = localMinIdx + 1
    while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
        rewards[rightIdx] = rewards[rightIdx - 1] + 1
        rightIdx += 1



# Solution #3
# O(n) time | O(n) space
def minRewards(score):
    rewards = [1 for _ in score]
    for i in range(1, len(score)):
        if score[i] > score[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed((range(len(score) - 1))):
        if score[i] > score[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)
