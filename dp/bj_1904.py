'''
def dpnum(k):
    if k >= 3:
        return dpnum(k-1) + dpnum(k-2)
    elif k == 2:
        return 2
    elif k == 1:
        return 1
    else:
        return 0
print(dpnum(num))
'''

import sys
input = sys.stdin.readline
num = int(input())
lst = [0]*num
lst[0] = 1
lst[1] = 2
for i in range(2,num):
    lst[i] = (lst[i-1] + lst[i-2])%15746
print(lst[-1])
