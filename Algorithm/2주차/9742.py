import sys

#sys.stdin = open("input.txt","r")

def dfs(lst,answer,nums):
    if len(lst) == len(nums):
        answer.append("".join(map(str,lst)))
    else:
        for i in nums:
            if i not in lst:
                lst.append(i)
                dfs(lst,answer,nums)
                lst.pop()
while True:
    try:
        lnums ,n= input().split()
    except :
        break
    nums = list(lnums)
    n = int(n)
    lst = []
    answer = []
    dfs(lst,answer,nums)
    try:
        print("{} {} = {}".format(lnums,n,answer[n - 1]))
    except:
        print("{} {} = {}".format(lnums,n,"No permutation"))


