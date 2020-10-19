print('Program to check whether the number is prime number or not ')
'''
A positive number(integer) greater then 1.
which has no other factors except one and the number itself is called a prime number
'''
number = int(input('Enter the number here :- '))

#checking whether the number is prime or not
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
        else:
            print(number, "is a prime number")
            break
    else:
        print(number, "is not a prime number")
#NOTE:- NEEDS SOME CHANGES : to show factors of the entered number when it is not a prime number