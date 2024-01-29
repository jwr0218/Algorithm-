import heapq
import sys

input = sys.stdin.readline

N = int(input())
c = list(map(int,input().split()))
M = int(input())
bs = list(map(int,input().split()))
boxes = []
for b in bs:
    heapq.heappush(boxes,b)
c.sort(reverse=True)
print(c)
exit()



if max(boxes) > max(c) :
    print(-1)
    exit()
    
total = 0
while len(boxes)>0:
    # Break Method
    total+=1
    
    for i in range(len(c)):
        if len(boxes) ==0 :
            break
        light_box = heapq.heappop(boxes)
        print(light_box)
        if light_box> c[i]:
            # print(c[i],'crain works!')
            heapq.heappush(boxes,light_box)

print(total)
    