def calculator():
 while True:
    print('Calculator')
    number1 = float(input('first number: '))
    operator = input("operator (+,-,*,/): ")
    number2 = float(input('second number: '))

    if operator == '+':
        print(number1 + number2)
    elif operator == '-':
        print(number1 - number2)
    elif operator == '*':
        print(number1 * number2)
    elif operator == '/':
        if number2 == 0:
            print('I cannot divide by zero')
        else:
            print(number1 / number2)
    else:
        print("I can't do this mathematics")
    again = input("Do you want to continue? (y/n): ")
    if again.lower() == 'n':
       break


