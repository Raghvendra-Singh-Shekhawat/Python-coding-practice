# Greatest of two numbers:


N1 = int(input("Enter the first number : "))
N2 = int(input("Enter the second number : "))

diff = N1 - N2

if diff < 0:
    print(f"{N2} is greater")
elif diff > 0:
    print(f"{N1} is greater")
elif diff == 0:
    print("Both the numbers are same")


#  Method 2

# print(max(N1,N2))