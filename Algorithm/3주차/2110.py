import sys
input = sys.stdin.readline
n , c = map(int,input().split())
home = []
answer = 0

for i in range(n):
    home.append(int(input()))

home.sort()
start  = 0
end = home[-1]-home[0]

while start <= end :

    mid = (start + end) // 2
    #맨 앞집에 하나 설치하고
    now = home[0]
    cnt = 1

    for i in range(len(home)):
        if home[i] >= now + mid:
            cnt +=1
            now = home[i]

    #print(cnt)
    if c <= cnt:

        #mid 가 작다 <- 더 넓게 만들어야 한다.
        start = mid +1  # < 끝내는 알고리즘
        answer = mid # answer 즉 두 집 사이의 거리가 가장 올바른걸 찾아야 한다...라,..
    else:
        #좁혀져야한다.
        end = mid -1

        # mid가 크다

print(answer)