'''  *         *
     *         *
     *         *
     *         *
     *         *  '''

rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(rows):
        if j == 0 or j == 4:
          print("*", end=" ")
        else:
           print(" ", end=" ")
    print()