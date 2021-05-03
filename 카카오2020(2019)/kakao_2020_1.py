input_text = "xababcdcdababcdcd"
lst_final = []
for j in range(1, len(input_text) // 2 + 1):  # 몇개의 문자를 쓰는가?
    # print(input_text)
    text_1 = input_text
    previous_sl = ""
    dic = {}
    s = ""

    for i in range(0, len(input_text), j):  # 어디서부터 시작하는가?
        sl = input_text[i:i + j]
        # print("SL :",sl)
        if previous_sl == sl:
            continue

        # print(sl)

        text = input_text[i + j:]
        count = 1

        while len(text) != 0:
            #    print("text : ",text[:j])
            if text[:j] == sl:
                count += 1
            else:
                break
            text = text[j:]

        previous_sl = sl;

        if count > 1:
            replace_s = str(count) + sl

            text_1 = text_1.replace(sl * count, replace_s, 1)

    lst_final.append(text_1)

min(list(map(lambda x: len(x), lst_final)))





