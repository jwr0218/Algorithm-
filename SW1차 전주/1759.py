import sys
input = sys.stdin.readline

L , C  = map(int,input().split())


char  = input().split()

char.sort()

#print(char)

vows = ['a', 'e', 'i', 'o', 'u']

answer = []

def dfs(st,idx):
    global L
    if len(st) == L :
        cnt = 0
        for i in st:
            if i in vows:
                cnt+=1
        #print(cnt)
        if 1<= cnt and cnt  <= L-2:
            answer.append(st)
    else:
        for i in range(idx,len(char)):
            value = st + char[i]
            dfs(value,i+1)


dfs("",0)

for i in answer:
    print(i)

