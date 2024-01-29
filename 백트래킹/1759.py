import sys
input = sys.stdin.readline

L , C = map(int, input().split())
alphabets = input().split()
alphabets.sort()
answer = []
vowels = ['a','e','i','o','u']
def dfs(s,idx):
    global L 
    if len(s) == L:
        # 모음 검사 .
        tmp = 0 

        for v in vowels:
            if v in s:
                tmp +=1
            
                
        if tmp >0 and tmp <L-1:    
            answer.append(s)
    else:
        for new_idx in range(idx,len(alphabets)):
            tmp_s = s+alphabets[new_idx]
            dfs(tmp_s,new_idx+1)    
        
    
    
s = ''
idx = 0 
dfs(s,idx)
for a in answer:
    print(a)