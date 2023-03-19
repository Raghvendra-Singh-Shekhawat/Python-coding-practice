#  Positive or Negative number :

number = int(input("Enter the number: "))

if number < 0:
    print(f"The {number} is negative.")
elif number > 0:
    print(f"The {number} is positive")
else:
    print("number is neither positive or negative")