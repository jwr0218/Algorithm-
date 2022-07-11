import sys
import heapq
from collections import deque

input = sys.stdin.readline

N = int(input())


heap = []
for i in range(N):
    n = int(input())


    if n == 0 :
        if len(heap) == 0 :
            print(0)
        else:
            print(heap.pop(-1))
    else:
        if len(heap) == 0 :
            heap.append(n)
        else:
            left = 0
            right = len(heap)-1
            while left <= right:
                mid = (left + right)//2
                if heap[mid] > n :
                    right = mid -1
                else:
                    left = mid + 1

            heap.insert(left,n)
    #print(heap)
    #print('==========')