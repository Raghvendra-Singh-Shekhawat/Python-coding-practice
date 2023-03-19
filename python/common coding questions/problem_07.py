# Greatest of the Three numbers:

N1 = int(input("Enter the first number : "))
N2 = int(input("Enter the second number : "))
N3 = int(input("Enter the  third number : "))


####### METHOD - 1

greatest = max(N1,N2,N3)
print(f"{greatest} is the greatest of the three numbers")


######  METHOD - 2

if N1 > N2 and N1 > N3:
    print(N1)
elif N2 > N1 and N2 > N3:
    print(N2)
elif N3 > N1 and N3 > N2:
    print(N3)
else:
    print("All the numbers are same")
