import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n+1):
    for j in range(n-i+1):
        for z in range(n-i-j+1):
            for y in range(n-i-j-z+1):

                t = i+j+z+y
                if t == n:
                    #print(i, j, z, y)

                    num = 1* i + 5 * j +z * 10 + y * 50

                    if num not in lst:
                        lst.append(num)
lst.sort()
#print(lst)
print(len(lst))
