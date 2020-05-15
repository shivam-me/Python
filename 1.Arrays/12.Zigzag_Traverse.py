'''
## Zigzag Traverse

#### Problem Statement


Write a function that takes in a two-dimensional array and returns a one-dimensional array of all the array's
elements in zigzag order. Zigzag order starts at the top left corner of the two-dimensional array, goes down
by one element, and proceeds in a zigzag pattern all the way to the bottom right corner.


Sample input:
[
[1, 3, 4, 10],
[2, 5, 9, 11],
[6, 8, 12, 15],
[7, 13, 14, 16],
]
Sample output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#### Solution

'''

# Time O(n) | Space O(n) >> where n is the total number of elements in 2D array
def zigzagTraverse(array):
    height = len(array) - 1 # 3
    width = len(array[0]) - 1 # 3
    result = []
    row, col = 0, 0
    goingDown = True
    while not isOutOfBound(height, width, row, col):
        result.append(array[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if col == width or row == 0:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    return result


def isOutOfBound(height, width, row, col):
    return row < 0 or row > height or col < 0 or col > width

arr = [
[1, 3, 4, 10],
[2, 5, 9, 11],
[6, 8, 12, 15],
[7, 13, 14, 16],
]
print(zigzagTraverse(arr))
