n = int(input())
lst = []
for i in range(n):
    s = input()
    if s in lst:
        continue
    lst.append(s)
d = list(map(len,lst))
arr = [[i,z] for i , z in zip(lst,d)]
#print(arr)
arr.sort(key = lambda x:x[0])
arr.sort(key = lambda x:x[1])
#print(d)
for i in arr:
    print(i[0])

