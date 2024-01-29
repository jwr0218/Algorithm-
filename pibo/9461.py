import sys
import heapq
input = sys.stdin.readline

T = int(input())



lst = [1,1,1,2,2,3]
def pibo(N):
    if N < 5 :
        return lst[N]
    return pibo(N-1) + pibo(N-1)


for i in range(T):
    N = int(input())
    print(pibo(N))