import sys
import queue
import heapq

T = int(input())
card = []
for i in range(T):
    heapq.heappush(card,int(input()))


total_search = 0 

while len(card) >1 :

    first_card = heapq.heappop(card)
    second_card = heapq.heappop(card)
    # print(first_card)
    # print(second_card)
    # print('==='*20)
    last = first_card + second_card
    total_search += last
    heapq.heappush(card,last)

print(total_search)

