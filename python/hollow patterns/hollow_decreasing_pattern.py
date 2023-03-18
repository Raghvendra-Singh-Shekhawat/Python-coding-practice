'''   * * * * *
      *     * 
      *   * 
      * * 
      *    '''  


rows = int(input("Enter the number of rows : "))

for i in range(rows):
    for j in range(i,rows):
        if j == i or i == 0 or j == rows-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()