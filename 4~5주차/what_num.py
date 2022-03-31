import sys
import heapq

input = sys.stdin.readline
N = int(input())

leftHeap=[] # 최대 힙, 중간값보다 작은값이 들어감

rightHeap=[] # 최소 힙 중간값보다 큰 값이 들어

for i in range(N):
    inputNum = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap,(-inputNum,inputNum)) # 최대 힙 만드는 방
    else:
        heapq.heappush(rightHeap, (inputNum, inputNum))# 최소 힙 만드는 방법

    if rightHeap and leftHeap[0][1] > rightHeap[0][1]:
        # 최소 힙이 있고, 왼쪽 리스트 최대 값이 오른쪽 리스트 최소값보다 클 때 수정을 해줘야 한다!
        #이를 밑 코드로 해결하였음
        min = heapq.heappop(rightHeap)[0]
        max = heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap,(-min,min))
        heapq.heappush(rightHeap, (max,max))
    #print("INPUT NUM : ",inputNum)
    #print("LEFT HEAP",leftHeap)
    #print("RIGHT HEAP ",rightHeap)
    print(leftHeap[0][1])