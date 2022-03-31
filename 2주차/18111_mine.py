import sys

def get_avg(Map):
    avg = 0
    for i in Map:
        avg += sum(i) / len(i)
    avg = round(avg/N)
    return avg

def check(Map):
    ch = True
    pre = Map[0][0]
    cc = False
    for i in range(len(Map)):
        if cc == True:
             break
        for j in range(len(Map[0])):
            if pre != Map[i][j]:
                cc = True
                ch = False
                break
    return ch
input = sys.stdin.readline
N, M , B = map(int,input().split())
Map = []
avg = 0
for i in range(N):
    temp_list = list(map(int,input().split()))
    Map.append(temp_list)

ch = False
t = 0
avg = get_avg(Map)
while ch == False:
    #print(avg)
    for i in range(len(Map)):
        for j in range(len(Map[0])):
            if avg == Map[i][j]:
                pass
            elif avg < Map[i][j]:
                gap = Map[i][j] - avg
                Map[i][j]-= gap

                B += Map[i][j]-avg
                t+= gap*2

            else:
                gap = avg - Map[i][j]

                if B > gap:

                    Map[i][j] += gap
                    t += gap
                else:
                    avg -=1
    ch = check(Map)
#    print("=======")
#    print(Map)
#    print(avg)


print(t,Map[0][0])



