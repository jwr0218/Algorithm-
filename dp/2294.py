import sys
input = sys.stdin.readline

n , k = map(int,input().split())

value = []
for i in range(n):
    v = int(input())
    if v > k :
        continue
    value.append(v)

value.sort()

dp = [99999999999 for _ in range(k+1)]
dp[0] = 0


for v in value:
    for idx in range(v,len(dp)):
        dp[idx] = min(dp[idx-v]+1 , dp[idx])


# print(dp)
if dp[-1] == 99999999999:
    print(-1)
else:
    
    print(dp[-1])