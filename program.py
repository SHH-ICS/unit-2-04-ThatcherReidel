# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

for number in range(1, 33):
    found = False
    if number % 3 == 0:
        found = True
        print("Fizz", end = "")
    if number % 5 == 0:
        found = True
        print("Buzz", end = "")
    if found == False:
        print("%d" % (number))
    else:
        print("")