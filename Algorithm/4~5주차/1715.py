import sys
import heapq

input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    heapq.heappush(lst,int(input()))

s = 0
while lst:
    value1 = heapq.heappop(lst)
    try:
        value2 = heapq.heappop(lst)
        two_sum = value2+value1
        s +=two_sum
        heapq.heappush(lst,two_sum)
    except:

        break
print(s)
