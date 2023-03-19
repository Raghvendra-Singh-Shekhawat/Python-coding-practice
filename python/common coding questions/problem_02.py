#  Even or Odd number:

number = int(input("Enter the number: "))

if number % 2 == 0:
    print(f"{number} is even")
elif number % 2 != 0:
    print(f"{number} is odd")