N , M = map(int,input().split())
times = list(map(int,input().split()))

# N = 멀티탭
# M = 멀티탭 사용 횟수
d = dict()
for _ in range(1,M+1):
    d[_] = 0 

taps = []

answer = 0
for t in range(len(times)):
    
    if times[t] in taps:
            continue
    
    if len(taps) < N:
        
        taps.append(times[t])
    else:
            
        dist = [9999 for _ in taps]
        for tap in range(len(taps)):
            for i in range(t,len(times)):
                if times[i] == taps[tap]:
                    dist[tap] = i -t
                    break
        
        idx = -1
        distance = -1
        # 가장 먼 것 삭제 
        
        for i in range(len(dist)):
            if distance < dist[i]:
                distance = dist[i]
                idx = i 

        taps[idx] = times[t]

        # print(taps)
                    
        answer +=1 
        
print(answer)