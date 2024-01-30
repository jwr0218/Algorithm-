import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
lst = []

lst2 = []
for _ in range(N):
    num = int(input())
    if num > 0:
        lst.append(num)
    else:
        lst2.append(num)
lst.sort(reverse=True)
lst2.sort()

#print(lst)
#print(lst2)
after= 0
def greed(num1,num2):
    if num1 + num2 > num1*num2:
        return num1 + num2
    else:
        return num1*num2

while len(lst) > 1 :
    num1 = lst.pop(0)
    num2 = lst.pop(0)
    after+=greed(num1, num2)
    #print(after)
while len(lst2) >1 :
    num1 = lst2.pop(0)
    num2 = lst2.pop(0)
    after += greed(num1, num2)
    #print(after)
after +=sum(lst)+sum(lst2)

print(after)

