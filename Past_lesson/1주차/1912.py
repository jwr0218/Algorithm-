
n = int(input())
lst = list(map(int,input().split(" ")))

dp = [0 for _ in range(n)]
dp[n-1] = lst[n-1]
for i in range(n-2,-1,-1):
    t = lst[i] + dp[i+1]
    if t > lst[i] :
        dp[i] = t
        #print(dp)
    else:
        dp[i] = lst[i]
        #print(dp)
#print(dp)
print(max(dp))


