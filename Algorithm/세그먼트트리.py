import sys
import heapq
input = sys.stdin.readline

N , M , K = map(int,input().split())

arr = [0] * (N+1)
tree = [0] * (N+1)

def prefix_sum(i):
    result = 0
    while i > 0:
        result +=tree[i]
        #가장 인접한 짝수 인덱스까지 더하겠다..
        i-= (i&-i)

    return result

def update(i,dif):
    while i <= N:
        tree[i] +=dif
        i +=(i & -i)


def interval_sum(start,end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1,N+1):
    x = int(input())
    arr[i] = x
    update(i,x)

print(tree)
for i in range(M+K):
    a, b, c = map(int,input().split())

    if a == 1:
        #업데이트
        update(b,c-arr[b])
        arr[b] = c
    else:
        print(interval_sum(b,c))