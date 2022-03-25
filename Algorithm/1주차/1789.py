S = int(input())
sum = 0
n = 1
while True:
    sum += n

    if sum > S:
        print(n-1)
        #print(sum)
        break
    n += 1

