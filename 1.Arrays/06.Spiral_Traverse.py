'''
 Spiral_Traverse

#### Problem Statement

Write a function that takes an N x M 2-D Array(that can be square shaped if n==m) and returns a one-dimensional array of all the array
elements in spiral order.

Spiral order starts at the top left corner of 2-D Array ,goes to the right, and proceeds in spiral pattern all the way until every
element has been visited.

Sample Input: [
          Top-[1,2,3,4],
              [12,13,14,5],
              [11,16,15,6],
       Bottom-[10,9,8,7],
              ]|      |
              Left  Right

Sample Output: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

'''
# Method 1
def spiralOrder(A):
    # T =Top , B = Bottom , L = Left , Right
    T,B,L,R = 0,len(A)-1,0,len(A[0])-1
    dir = 0
    ans = []
    while(T <= B and L <= R):

        if(dir == 0):
            for i in range(L,R+1):
                ans.append(A[T][i])
            T+=1
        elif(dir == 1):
            for i in range(T, B+1):
                ans.append(A[i][R])
            R -= 1
        elif(dir == 2):
            for i in range(R,L-1,-1):
                ans.append(A[B][i])
            B -= 1
        elif(dir == 3):
            for i in range(B,T-1, -1):
                ans.append(A[i][L])
            L += 1
        dir = (dir+1) % 4

    return ans



# Method 2
def spiralOrders(matrix):
    # T =Top , B = Bottom , L = Left , Right
    T, B, L, R = 0, len(matrix)-1, 0, len(matrix[0])-1
    ans = []
    while(T <= B and L <= R):
        for i in range(L, R+1):
            ans.append(matrix[T][i])
        T += 1

        for i in range(T, B+1):
            ans.append(matrix[i][R])
        R -= 1

        for i in range(R, L-1, -1):
            ans.append(matrix[B][i])
        B -= 1

        for i in range(B, T-1, -1):
            ans.append(matrix[i][L])
        L += 1

    return ans


matrix = [
           [1, 2, 3, 4],
           [12, 13, 14, 5],
           [11, 16, 15, 6],
           [10, 9, 8, 7],
         ]
print(spiralOrders(matrix))
