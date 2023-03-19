#  Prime number:

number = int(input("Enter the number: "))
prime = 0
for i in range(2,number):
    if number%i == 0:
        prime = 1
        break

if number <= 2:
    print("prime")
elif prime == 1:
    print("no prime")
elif prime == 0:
    print("prime")