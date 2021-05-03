input_s = "()))((()"


def flip(s):
    if s == "(":
        return ")"
    elif s == ")":
        return "("
    else:
        return ""


def flipString(s):
    cnt = 0

    find = ""
    while cnt < len(s):
        find += flip(s[cnt])
        cnt += 1

    return find


def find_right(s):
    state = 0
    cnt = 0;

    while cnt < len(s):
        if s[cnt] == "(":
            state += 1
        elif s[cnt] == ")":
            state -= 1
        else:
            pass

        cnt += 1

        if state < 0:
            return False
        else:
            return True


def fun(s):
    state = 0
    cnt = 0;

    while cnt < len(s):
        if s[cnt] == "(":
            state += 1
        elif s[cnt] == ")":
            state -= 1
        else:
            pass

        cnt += 1

        if state == 0:
            break

    if state == 0:
        s_1 = s[:cnt]  #

        s_2 = s[cnt:]

        print("s : ", s)
        print("s_1 :", s_1)

        print("s_2 :", s_2)
        print("===========")

        # ========================스트링 자르기===================

    if len(s_2) == 0:
        v = ""
    else:
        v = fun(s_2)
    ## =========================== v ============

    if find_right(s_1):
        u = s_1  # 올바르다.
        print("u+v :", u + v)
        return u + v

    else:

        # 올바르지 않다.

        string = "(" + v + ")"
        print("string : ", string)
        u = s_1[1:-1]
        print("u : ", u)
        if len(u) == 0:
            print("u's length is 0 ")

            return string
        else:
            a = flipString(u)
            print("a : ", a)

            print("string + flipString", string + a)
            return string + flipString(u)

        # divide(s_2)


print(fun(input_s))
