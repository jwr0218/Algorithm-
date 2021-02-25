
def greed(lst,L):
    lst.sort()
    sum = 0
    cnt_start = 0
    cnt_end = 0
    while True:
        length = lst[cnt_end] - lst[cnt_start] + 1
        print("===")
        print(sum)
        print("st :", lst[cnt_start], " end : ", lst[cnt_end])


        if length <= L :
            sum +=0


            if cnt_end == len(lst) - 1:
                sum += 1
                break
            cnt_end += 1
        else:
            sum += 1

            if cnt_end == len(lst)-1:

                sum +=1
                break

            cnt_start = cnt_end



    return sum

if __name__ == '__main__':
    N = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    print(greed(lst,N[1]))
