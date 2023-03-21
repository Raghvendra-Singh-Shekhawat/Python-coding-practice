# Prime number within a given range:

N1 = int(input("Enter the lower number: "))
N2 = int(input("Enter the higher number: "))



for i in range(N1,N2+1):
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i, end=" ")
    

    
 


