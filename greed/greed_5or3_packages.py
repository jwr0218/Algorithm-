# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def greed(N):
    min = [10**4,10**4]
    for i in range(0,N//5+1):
        num = N
        zip_5 = i
        num = num - 5*i
        zip_3 = num // 3

        s = zip_5 + zip_3
        if s < sum(min) and num % 3 == 0:
            min = [zip_5,zip_3]


    if sum(min) == 20000 :
        return -1

    else:
        return sum(min)











# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(greed(18))
    print(greed(4))
    print(greed(6))
    print(greed(9))
    print(greed(11))
    print(greed(int(input())))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
