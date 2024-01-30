import sys

n,m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

lst = []
answer = []
def dfs():

    #베이스 케이스
    if len(lst) == m:
        s = " ".join(map(str,lst))
        if s not in answer:
            print(s)
            answer.append(" ".join(map(str,lst)))
    else:
        for i in nums:
            if i >= lst[-1]:

                lst.append(i)
                dfs()
                lst.pop()
nums.sort()
for i in nums:
    lst = [i]

    dfs()
