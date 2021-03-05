N = int(input())
lst = []
for i in range(N):
    l = list(map(int, input().split()))
    lst.append(l)

cnt = -1
s = 0

#max(lst+lst[0+1])
for i in range(N-2,-1,-1):
    for j in range(len(lst[i])):
        lst[i][j] = max(lst[i+1][j],lst[i+1][j+1]) + lst[i][j]



print(lst[0][0])




