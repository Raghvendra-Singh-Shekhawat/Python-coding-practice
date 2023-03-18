'''       *         
          *         
      * * * * *   
          *         
          *         '''

rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(rows):
        if j == int(rows/2) or i == int(rows/2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()