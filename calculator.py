class Calculator:
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b
    def calculator(self):
            while True:
                print('Calculator')
                number1 = float(input('first number: '))
                operator = input("operator (+,-,*,/): ")
                number2 = float(input('second number: '))

                if operator == '+':
                    print(self.addition(number1,number2))

                elif operator == '-':
                    print(self.subtraction(number1,number2))
                elif operator == '*':
                    print(self.multiplication(number1,number2))
                elif operator == '/':
                    if number2 == 0:
                        print('I cannot divide by zero')
                    else:
                        print(self.division(number1,number2))
                else:
                    print("I can't do this mathematics")
                again = input("Do you want to continue? (y/n): ")
                if again.lower() == 'n':
                    break


