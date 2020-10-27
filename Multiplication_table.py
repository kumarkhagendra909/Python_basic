print("Program for creating Multiplication table of a number ")
number = int(input("Enter the number  for which you need a table :- "))
count = 1
print("Multiplication table for : ", number)
for count in range(1,11):
    print(number, "*", count, "=", (number * count))
