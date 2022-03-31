
Nd  = list(map(int,input().split()))
L = 0
R = 0


while Nd[0] > 1 or Nd[1] > 1 :
    if Nd[1] > Nd[0]:
        R +=Nd[1]//Nd[0]
        Nd[1] = Nd[1] % Nd[0]
    #    print("After 1 : ",Nd)
    elif Nd[0] > Nd[1]:
        L += Nd[0]//Nd[1]
        Nd[0] = Nd[0] % Nd[1]
    #    print("After 2 : ", Nd)

L += Nd[0]-1
R += Nd[1]-1

print(L,R)
