
import sys
input = sys.stdin.readline
n = int(input())
C = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))
C.sort(reverse = True)
B.sort(reverse = True)

if B[0] > C[0] :
    print(-1)
    exit()
time = 0
while len(B) > 0:
    time += 1
    for i in C:
        for k in range(len(B)):
            if i >= B[k]:
                B.pop(k)
                break

print(time)

