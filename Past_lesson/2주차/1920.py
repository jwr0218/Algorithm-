import sys
import bisect
input = sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))
lst.sort()
M = int(input())
lst2 = list(map(int,input().split()))
left = 0
right = len(lst)-1
for target in lst2:
    left = 0
    right = len(lst)-1
    cnt = 0

    while True:

        if left > right:
            print(0)
            break

        mid = (left + right) // 2
        if lst[mid] == target:
            print(1)
            break
        elif lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1