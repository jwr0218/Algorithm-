import sys

n,m = map(int,sys.stdin.readline().split())

lst = []


def dfs():
    #베이스 케이스
    if len(lst) == m:
        print(" ".join(map(str,lst)))
    else:
        for i in range(n+1):
            if i not in lst:
                lst.append(i)
                dfs()
                lst.pop() # 이미 있었으니까 빼기

lst = []
dfs(1)