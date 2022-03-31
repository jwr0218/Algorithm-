n = int(input())

ans = 0
row = [0 for _ in range(n)]

# 인덱스 관계를 활용해서 표했다.
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True

# 인덱스 하나로 퀸이 어디에 놓이는지 확인할 수 있음
# 추가 궁금점 - row[0] 에는 무조건 놓이는 알고리즘임,,, 이게 오류가 되진 않나?

def n_queens(x):
    global ans
    if x == n:
        ans += 1

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)


n_queens(0)
print(ans)