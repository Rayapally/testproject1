def fizzbuzz(number):
    if (number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif(number % 3 == 0):
        print("Buzz")
    elif(number % 5 == 0):
        print("Fizz")
    else:
        print(number)

number = int(input("Enter the number : "))
fizzbuzz(number)