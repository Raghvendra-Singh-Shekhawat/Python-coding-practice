'''      * 
         * * 
         * * *
         * * * *
         * * * * *      
         * * * *
         * * *
         * * 
         *   '''  


rows = int(input("Enter the number of rows: "))

for i in range(rows-1):
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(rows):
    for j in range(i, rows):
        print("*", end=" ")
    print()