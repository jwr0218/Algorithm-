import sys


def greed(lst, k):
    lst.sort()

    new_min = []
    for i in lst:
        new_min.append(i * k)
        k = k - 1
    m = max(new_min)
    return m


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    max_lst = []
    for i in range(N):
        max_lst.append(int(sys.stdin.readline()))
    print(greed(max_lst, N))




