print("program for fibonacci series ")
n_term = int(input("Enter your number of terms for sequence :- "))
first_number = int(input('Enter your first number :- '))
second_number = int(input("Enter your second number :- "))
count = 0
if n_term <= 0:
    print(" Please enter a positive integer ")
elif n_term == 1:
    print(" fibonacci sequence upto ", n_term, ":-", first_number)
else:
    print("fibonacci sequence upto ", n_term, ":")
    while count < n_term:
        print(first_number, end=',')
        n_next = first_number + second_number
#updating values ...........................
        first_number = second_number
        second_number = n_next
        count += 1
print("\n")

