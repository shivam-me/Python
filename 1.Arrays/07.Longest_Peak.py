'''
        LONGEST PEAK

PROBLEM STATEMENT:

Write a function that takes array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a
tip(the highest value in the peak) at which point they become strictly decreasing.At least three integers
are required to form a peak. For Example,the integers 1,4,10,2 form a peak,but the integers 4,0,10 don't
and neither do the integers 1,2,2,0. Similarly,the integers 1,2,3 don't form a peak because there aren't
any strictly decreasing integers after the 3.

Sample Input :

array = [1,2,3,4,0,10,6,5,-1,-3,2,3]

Sample Output :

6 # 0,10,6,5,-1,-3




'''

def longestPeak(array):
    longestPeakLen = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] > array[i + 1]
        if not isPeak:
            i += 1   # i will increment till 5th pos i.e 10 then isPeak=True
            continue

        leftIdx = i - 2 # -1 after 1st iteration

        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]: # 3<1
            leftIdx -= 1

        rightIdx = i + 2

        while rightIdx < len(array) and array[rightIdx - 1] > array[rightIdx]:
            rightIdx += 1

        currentPeakLen = rightIdx - leftIdx - 1
        longestPeakLen = max(longestPeakLen, currentPeakLen)
        i = rightIdx

    return longestPeakLen

# My Solution


def longestpeak(arr):
    i = 1
    ispeak = None
    peak_index = []
    peak_elements1 = []
    peak_elements2 = []
    while i < len(arr)-1:
        ispeak = arr[i-1] < arr[i] > arr[i+1]
        if ispeak:
            peak_index.append(i)   # Append the peak index value in list [3,5] i.e value 4 and 10
        i += 1
    longest_peak = 0
    for i in peak_index:
        curr_peak = 0
        j = i
        left_count = 0
        right_count = 0
        peak_elements1.append(arr[i]) # Append the root index value to peak elements
        while(arr[i] >= arr[i-1]): # Counting numbers to the left of index
            peak_elements1.append(arr[i-1])
            left_count += 1
            i -= 1
        while(arr[j] >= arr[j+1]):  # Counting numbers to the right of index
            peak_elements1.append(arr[j+1])
            right_count += 1
            j += 1
        curr_peak_len = left_count+right_count+1 # 1 because adding root index to currentpeak
        if(curr_peak_len > longest_peak):
            longest_peak = curr_peak_len
            peak_elements2 = peak_elements1
            peak_elements1 = []
    print(peak_elements2)
    return longest_peak


print(longestpeak([1, 2, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
