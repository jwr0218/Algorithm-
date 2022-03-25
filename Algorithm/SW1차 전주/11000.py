import sys
import heapq
input = sys.stdin.readline

n = int(input())
queue = []
for i in range(n):
    start , end = map(int,input().split())
    queue.append([start,end])

queue.sort()
#끝나는 시간을 넣어줌
room = []
heapq.heappush(room,queue[0][1])
#queue에서 정렬을 했기 때문에 queue에 순차적으로 넣어준다.
for i in range(1,n):
    #제일 먼저 끝나는 수업보다 현재 수업이 먼저 끝나는지?
    if queue[i][0] < room[0]:
        heapq.heappush(room,queue[i][1])

    else: #현재 강의실에서 수업을 계속 이어갈 수 있다?
        heapq.heappop(room)
        #이후 언재 끝날까?
        heapq.heappush(room,queue[i][1])
print(len(room))