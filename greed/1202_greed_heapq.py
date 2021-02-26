import heapq

N, K  = map(int,input().split())

M_V = []
for i in range(N):
    a =list(map(int, input().split()))
    M_V.append(a)

C = []
for i in range(K):
    C.append(int(input()))

C.sort()
#M_V.sort(key=lambda x:x[0])
M_V.sort()
print(M_V)
cnt = 0
s = 0
j = 0
max_heap = []
for i in range(K):

    while j<N and C[i]>=M_V[j][0]:
        heapq.heappush(max_heap,-M_V[j][1])
        j+=1

    if len(max_heap)>0:
        b = heapq.heappop(max_heap)
        s+=abs(b)

print(s)