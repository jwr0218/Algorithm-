n = int(input())
number = list(map(int,input().split()))
k = int(input())
lst = []
for k in range(k):
    a = list(map(int, input().split()))
    lst.append(a)


l = [[0]*n for k in range(n)]



for i in range(n):

    for start in range(n):
        end = start + i
        if end >= n:
            break;
        if start == end:
            l[start][end] = 1
            continue
        elif start +1 == end:
            if number[start] == number[end]:
                l[start][end] = 1
                continue
        elif start < end:
            if number[start] == number[end] and l[start+1][end-1]==1:
                l[start][end] = 1




for k in lst:
    print(l[k[0]-1][k[1]-1])












