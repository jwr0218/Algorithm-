import sys
input = sys.stdin.readline
n  = int(input())

dist = list(map(int,input().split()))
oil_price = list(map(int,input().split()))

total_dist = sum(dist)
min_lst = []

def processing(lst):

    print("lst pre : ", lst)
    lst_2 = []
    check = False

    while True:
        pre = lst[0]
        for j in range(len(lst)):
            if pre[0] < lst[j][0]:
                #print("index",j)
                #print(pre)
                #print(lst[j])
                #print("??",lst)
                re = lst[j]
                lst.remove(pre)
                lst.remove(re)
                lst.insert(0, [pre[0], re[j][1] + pre[1]])
                
                break
        else:
            break
    print("lst after : ",lst)




for i in range(n-1,-1,-1):
    if i == n-1 :
        pre_price = 10000000000

    else:

        if pre_price > oil_price[i]:

            distance= 0
            for j in min_lst:
                distance +=j[1]
            #print("distance ",distance)
            #print("rest_dist", total_dist-distance-sum(dist[:i]))

            min_lst.insert(0,[oil_price[i],total_dist - (sum(dist[:i]) + distance)])
            processing(min_lst)


cost = 0
for i in min_lst:
    cost +=i[0]*i[1]

print(cost)

