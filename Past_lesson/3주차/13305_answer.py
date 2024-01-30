import sys
input = sys.stdin.readline
n  = int(input())

dist = list(map(int,input().split()))
price = list(map(int,input().split()))

cost = 0
pre_price = price[0]
distance = dist[0]

for i in range(1,n-1):
    if price[i] < pre_price:

        cost += pre_price*distance
        distance = dist[i]
        pre_price = price[i]
    else:
        distance +=dist[i]
cost = cost+ pre_price * distance
print(cost)