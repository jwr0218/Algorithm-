#최소 스패닝
import sys

input = sys.stdin.readline

V , E = map(int,input().split())
edge = []
for i in range(E):
    edge.append(list(map(int,input().split())))

parent = [i for i in range(V)]

def find(a):
    if parent[a] ==a:
        return a
    parent[a] = find(parent[a])
    return parent[a]
#a,b의 부모를 합치기!
def union(a,b):
    a = find(a)
    b = find(b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b
edge.sort(key=lambda x : x[2])
total_weight = 0
for ed in edge:


    n1 = ed[0]-1
    n2 = ed[1]-1
    #print(parent)

    if find(n1) != find(n2):
        total_weight += ed[2]
        union(n1,n2)

print(total_weight)