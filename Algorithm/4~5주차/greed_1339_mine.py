import sys

input = sys.stdin.readline

n = int(input())
lst = []
lst2 =[]
for i in range(n):
    val = input().replace("\n","")
    lst.append(val)
    lst2.append(val)
lst.sort(key=len,reverse=True)

values = dict()
while len(lst)>0:
    lst.sort(key=len, reverse=True)
    v = lst.pop(0)
    l = 1
    if len(v) >1:

        num = v[0]
        l = len(v)
        v = v[1:]
        lst.append(v)
    else:
        num = v

    if num not in values:
        values[num] = [l,1]

    else:
        values[num][1] += 1

        continue
# 같은 자리에 처음 나왔는데 빈도가 훨신 많으면 얘를 사용해야 함
# 정렬 기준 - 자릿수 + 횟수
# 여기서부터는 똑같음, 위 알고리즘을 수정 할 것

n = 0


val = sorted(values.items(), key = lambda item: (item[1][0],item[1][1]), reverse = True)

final = [[x[0],x[1][0],x[1][1]] for x in val]
final.sort(key= lambda x:(x[1],x[2]),reverse=True)

#print(final)
z = 9
for s in final:
    for i in range(len(lst2)):
        lst2[i] = lst2[i].replace(s[0],str(z))
    z-=1

#print(lst2)
print(sum(list(map(int,lst2))))

