import sys
from collections import deque
import re



input = sys.stdin.readline
A = list(input().replace("\n",""))
B = list(input().replace("\n",""))

len1 = len(A)
len2 = len(B)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if A[i-1] == B[j-1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1

        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])
