import sys
import copy
input = sys.stdin.readline
n = int(input())
Map = [[" " for _ in range(n)] for _2 in range(n)]

def divide_conquer(n):
    global Map

    if n == 3:
        Map[0][:3] = ["*"] * 3
        Map[2][:3] = ["*"] * 3
        Map[1][:3] = ["*"," ","*"]

        return

    a = n // 3
    divide_conquer(n // 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a * i + k][a * j:a * (j + 1)] = Map[k][:a]





#crop = [row[j:j+m] for row in Map[i:i+n]]



divide_conquer(n)
for z in Map:
    print("".join(z))

