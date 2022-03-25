import sys

input = sys.stdin.readline

N,r,c  = map(int,input().split())


N = 2**N # 한 변

answer = 0




def z(N,x,y,answer):

    if x == 0 and y == 0  :

        answer +=1

        return answer

    else:
        #1사분면
        if N/2 > x and  N/2 > y :
            answer += z(N / 2, x , y, answer)

            return answer
        #2사분면
        elif N/2 <= x and N/2 >y:
            answer += N / 2 * N / 2 + z(N/2, x - N/2 , y , answer)

            return answer
        # 3사분면
        elif N / 2 > x and N / 2 <= y:
            answer += 2*(N/2*N/2) + z(N / 2, x , y- N/2 , answer)

            return answer

        elif N / 2 <= x and N / 2 <= y:
            answer += 3*(N / 2 * N / 2) + z(N / 2, x - N / 2, y - N/2, answer)

            return answer

    return False
print(int(z(N,c,r,answer)-1))