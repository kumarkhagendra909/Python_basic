print("Program for factorial of number : ")
number = int(input(" Enter your number to be a factorial : "))
factorial = 1
if number == 0:
    print("factorial of ", number, "is ", factorial)
elif number < 0:
    print("sorry thereis no factorial exist .......")
elif number > 0:
    for i in range(1, number + 1):
        factorial = factorial * i

print("factrorial of", number, "is :", factorial)

