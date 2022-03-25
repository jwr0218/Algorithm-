string = input()
flag = False
word = ""
answer = ""
for s in string:

    if flag == False:

        if s == "<":
            flag = True
            word +=s
        elif s == " ":
            word +=s
            answer +=word
            word = ""
        else:
            word = s+word
    else:
        word +=s
        if s == ">":
            flag = False
            answer += word
            word = ""
print(answer+word)