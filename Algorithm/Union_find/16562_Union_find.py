import sys
import heapq
input = sys.stdin.readline

N , M , K = map(int,input().split())

fee = list(map(int,input().split()))

parents = [i for i in range(N)]
check = [False for i in range(N)]

def find(a):
    if parents[a] == a:
        return a

    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if fee[a] < fee[b] :
        parents[b] = a
    else:
        parents[a] = b

for i in range(M):
    a , b = map(int,input().split())
    a -=1
    b -=1
    union(a,b)
s = 0

check = set()

for j in range(N):

    if find(j) not in check:
        s += fee[find(j)]
        check.add(parents[j])



if s > K:
    print("Oh no")

else:

    print(s)
