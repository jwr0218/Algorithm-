min , mx = map(int,input().split())
check = [True]*(mx+1-min+1)
check[0] = False



for i in range(2,mx+1):
    a = 0
    cnt = max( min//(i**2),1 )
    #print('계산 : ', min//(i**2))
    #print('제곱 : ', i**2)
    a = (i ** 2) * cnt
    while a <= mx:


        if a-min+1 > 0:

            check[a-min+1] = False

        cnt +=1
        a = (i ** 2) * cnt
    if i**2 > mx:
        break




#print(check)

print(sum(check))

