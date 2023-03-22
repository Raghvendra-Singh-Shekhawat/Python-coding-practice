# Armstrong number in a given range :

lower_number = int(input("Enter any positive number: "))
higher_number = int(input("Enter any positive number: "))



for i in range(lower_number,higher_number+1):
    sum = 0
    length = len(str(i))
    original = i

    while i > 0:
        digit = i % 10
        sum += digit ** length
        i = i // 10

    if sum == original:
        print (original ,end=", ")
   


