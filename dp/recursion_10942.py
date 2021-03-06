
def dynamic(number,lst):
    if len(lst) == 1:
        return 1
    elif len(lst) ==2:

        if number[lst[0]-1] == number[lst[1] - 1]:
            return 1
        else:
            return 0

    if number[lst[0]-1] != number[lst[-1] - 1]:

        return 0
    else:
        lst = lst[1:-1]
        return dynamic(number,lst)


n = int(input())
number = list(map(int,input().split()))
k = int(input())
lst = []
for k in range(k):
    a = list(map(int, input().split()))
    lst.append(a)



for l in lst:
    print(dynamic(n,number,l))












