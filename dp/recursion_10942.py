

def dynamic(n,number,lst):
    l = [[0]*n for k in range(n)]

    for i in range(n):
        end = start + i
        if end > n:
            break;
        if start == end:
            l[start][end] = 1
        if start +1 == end:


n = int(input())
number = list(map(int,input().split()))
k = int(input())
lst = []
for k in range(k):
    a = list(map(int, input().split()))
    lst.append(a)



for l in lst:
    print(dynamic(n,number,l))












