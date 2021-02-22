
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
    num = int(input())

    conference = []

    for i in range(num):
        conference.append(list(map(int, input().split())))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/





