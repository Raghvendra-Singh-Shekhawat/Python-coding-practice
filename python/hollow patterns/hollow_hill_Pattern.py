'''          * 
           *   * 
         *       *
       *           *
     * * * * * * * * *    '''     


rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(i,rows):
        print(" ", end=" ")
    for j in range(i):
        if i==rows-1 or j==0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(i+1):
        if i==j or i==rows-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()