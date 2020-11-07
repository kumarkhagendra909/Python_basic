"""
what is armstrong number ?
 --> Every positive integer of n - number of order is said to be as Armstrong number
 ie ->    lets say you have  ABCD...............  as your number which is equal to a++n + b**n + c**n + d**n + ......
  for eg :-  We have a number 153
  its order of n (total number digits) is 3
   153 = 1^3 + 5^3 + 3^3 = *153*
"""
#  Program to find Armstrong_number

lower = 100
upper = 2000
for number in range(lower, upper + 1):
    order = len(str(number))
    # initialising sum to be zero
    sum = 0
    #find the sum of the n of each digits
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if number == sum:
        print(number)
