n , m  = map(int,input().split())
matrix = []




for i in range(n):
    matrix.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        matrix[i][j] %=1000
def productMatrix(mat1, mat2):
    matR = [len(mat2[0]) * [0] for i in range(len(mat1))]

    for i in range(len(matR)):
        for j in range(len(matR[i])):
            for k in range(len(mat1[i])):
                matR[i][j] += mat1[i][k] * mat2[k][j]


            matR[i][j] %= 1000

    return matR


def divide_conquer(m):
    global matrix
    #print("M : ",m)
    if m == 1:
        return matrix
    elif m==2:
        return productMatrix(matrix,matrix)


    if m % 2 == 1:
        mt = divide_conquer(m // 2)
        mt = productMatrix(mt,mt)
        mt = productMatrix(mt,matrix)
    else:
        mt = divide_conquer(m//2)
        mt = productMatrix(mt,mt)
    return mt


mt = divide_conquer(m)
for i in mt:
    print(" ".join(map(str,i)))
