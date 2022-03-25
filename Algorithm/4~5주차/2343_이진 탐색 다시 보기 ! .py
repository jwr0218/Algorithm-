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
answer = 0
while start <= end :
    K = 1
    mid = (start + end ) //2
    s = 0
    for i in range(len(lst2)):
        if s +mid <= lst2[i] :
            s = lst2[i-1]
            K+=1
            #print(s)
    if M < K :
        # mid 가 작다.
        # mid가 커진다.
        start = mid +1
        answer = mid
    else:
        # mid가 크다.
        # mid가 작아진다.
        end = mid - 1


print(answer)