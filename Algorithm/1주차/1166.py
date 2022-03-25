N , L , W , H = map(int,input().split())

#print(N,L,W,H)

end = min([L,W,H])
start = 0
mid = 0
for i in range(10000):
    mid = (start + end) / 2
    a = L // mid
    b = W // mid
    c = H // mid

    if N <= a*b*c:
        start = mid
    else:
        end = mid

print(mid)