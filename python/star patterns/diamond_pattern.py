'''          * 
           * * * 
         * * * * *
       * * * * * * *
     * * * * * * * * *      
       * * * * * * *
         * * * * *
           * * * 
             *   '''     

rows = int(input("Enter the number of rows : "))

for i in range(rows-1):
    for j in range(i,rows):
        print(" ", end=" ")
    for j in range(i+1):
        print("1", end=" ")
    for j in range(i):
        print("2", end=" ")
    print()
for i in range(rows):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i+1,rows):
        print("*", end=" ")
    for j in range(i,rows):
        print("*", end=" ")
    print()