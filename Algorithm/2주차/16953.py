import sys
input = sys.stdin.readline
A , B   = map(int,input().split())
#print(A, B)
num = B
cnt = 0
while True:
    if A == num:
        break
    if A > num:
        cnt = -2
        break
    if num % 10 == 1:
        num = num // 10
        cnt +=1

    else:
        num = num/2
        cnt +=1
print(cnt+1)

