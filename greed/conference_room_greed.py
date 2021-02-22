
def greed( lst ):

    lst = sorted(lst, key=lambda a: a[0])
    lst = sorted(lst, key=lambda a: a[1])
    last = 0
    cnt = 0


    for i, j in lst:
        if i >= last:
            cnt += 1
            last = j

    return cnt


if __name__ == '__main__':
    num = int(input())

    conference = []

    for i in range(num):
        conference.append(list(map(int, input().split())))
    print(greed(conference))




