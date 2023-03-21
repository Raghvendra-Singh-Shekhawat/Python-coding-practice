# Palindrome number:  a number which is same when reversed

num = int(input("Enter the number: "))

number = num

rev = 0

while(number > 0):
    rev = (rev*10) + number % 10
    number = number//10
reverse = rev

if reverse == num:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")