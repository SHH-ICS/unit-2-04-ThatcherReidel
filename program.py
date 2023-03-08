# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

# start at 1 and end at 32  
for number in range(1, 33):
    # start with an empty string so we can tell later if fizz or buzz was added
    value = ""
    if number % 3 == 0:
        # it's a multiple of 3 so add Fizz
        value += "Fizz"
    if number % 5 == 0:
        # it's a multiple of 5 so add Buzz
        value += "Buzz"
    # if the value is still an empty string replace it with the number
    if len(value) == 0:
        value = str(number)
    # output the value to the screen
    print(value)