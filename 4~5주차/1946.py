T = int(input())

for _ in range(T):
    lst = list()
    n = int(input())
    for i in range(n):
        lst.append(list(map(int,input().split())))

    paper_min = 0
    interview_min = 0

    paper_descend = sorted(lst,key = lambda x:x[0])
    #print(paper_descend)
    interview_min = paper_descend[0][1]

    #print("paper : ",paper_min)
    #print("interview : ",interview_min)
    #print(paper_descend)
    #print(interview_descend)
    cnt = 1
    for i in paper_descend:
        if i[1] < interview_min:
            interview_min = i[1]
            cnt +=1

    print(cnt)
