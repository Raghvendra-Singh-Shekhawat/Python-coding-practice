'''          * 
           *   * 
         *       *
       *           *
     *               *      
       *           *
         *       *
           *   * 
             *   '''     

rows = int(input("Enter the number of rows : "))

for i in range(rows-1):

    for j in range(i,rows):
        print(" ", end=" ")

    for j in range(i+1):
        if j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    for j in range(i):
        if j == i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


for i in range(rows):
    
    for j in range(i+1):
        print(" ", end=" ")

    for j in range(i,rows):
        if j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    for j in range(i,rows-1):
        if j == rows-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()