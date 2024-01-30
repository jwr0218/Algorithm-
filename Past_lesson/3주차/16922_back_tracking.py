import sys
input = sys.stdin.readline
n = int(input())
alpha = [1,5,10,50]
answer = []
def dfs(roma,c):
    global n
    c += 1
    test = []
    for i in alpha:
        roma_n = roma+i
        if roma_n not in test:
            test.append(roma_n)
            #여기서 좀 줄이는 방법을 찾아야 하겠다..
            if c == n:
                #val = calculate(roma_n)
                if roma_n not in answer:
                    answer.append(roma_n)
            else:
                dfs(roma_n,c)
dfs(0,0)
#print(answer)
print(len(answer))





################# 지수님 dfs 해결

N = int(input())
l = [1,5,10,50]
s = []
result = []
def dfs(flag):
    if len(s) == N:
        a = sum(s)
        result.append(a)
        return

    for j in range(flag,4): # 여기서 조건을 줬다.
        s.append(l[j])
        dfs(j)
        s.pop()

dfs(0)
result = list(set(result))
print(len(result))

