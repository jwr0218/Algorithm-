N , M  = map(int,input().split())

lst = list(map(int,input().split(" ")))
lst2 = []
s = 0
for i in lst:
    s = s+i
    lst2.append(s)

#print(lst2)
start = max(lst)
end = lst2[-1]
answer = 10000000000
while start <= end :
    mid = (start + end) // 2
    K = 1
    s = 0
    for i in range(len(lst)):
        if s + lst[i] > mid:
            K +=1
            s = 0
#-===== 뭔차일까?
        s += lst[i]
    if M < K :
        # mid 가 작다.
        # mid가 커진다.
        start = mid +1


    else:
        answer = min(answer,mid)
        # mid가 크다.
        # mid가 작아진다.
        end = mid - 1


print(answer)