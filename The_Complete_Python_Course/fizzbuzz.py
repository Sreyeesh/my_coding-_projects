"""
# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

do multiples of 2 do multiples of 6  do multiples of 2 and 6 

"""
numbers = range(1,101)

for number in numbers:
    if number % 3 == 0 and number % 5  == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
