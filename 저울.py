# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def greed(size , lst ):

    lst.sort()
    sum = 0
    for i in range(size):

        if sum+1 >= lst[i]:
            sum +=lst[i]

        else:
            break

    return sum_num+1



if __name__ == '__main__':
    size = int(input())
    lst = list(map(int,input().split()))
    print(greed(size,lst))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
