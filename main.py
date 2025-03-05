def fizzBuzz(number):
    if (number % 3 == 0 and number % 5 == 0):
        return "FizzBuzz"
    elif (number % 3 == 0):
        return "Fizz"
    elif (number % 5 == 0):
        return "Buzz"
    else:
        return number
def printFizzBuzz():
    for i in range(1,101):
        print(fizzBuzz(i))
printFizzBuzz()
