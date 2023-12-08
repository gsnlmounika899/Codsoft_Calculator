class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Addition(self):
        try:
            return self.x + self.y
        except TypeError as e:
            print(f"Error: {e}")
            return None

    def Subtraction(self):
        try:
            return self.x - self.y
        except TypeError as e:
            print(f"Error: {e}")
            return None

    def Multiplication(self):
        try:
            return self.x * self.y
        except TypeError as e:
            print(f"Error: {e}")
            return None

    def Division(self):
        try:
            if self.y == 0:
                raise ZeroDivisionError("Division by 0 is not possible")
            return self.x / self.y
        except (TypeError, ZeroDivisionError) as e:
            print(f"Error: {e}")
            return None

def Input(a):
    while True:
        try:
            return float(input(a))
        except ValueError:
            print("Invalid input. Please enter a valid Number.")

while True:
    x = Input("Enter the first number: ")
    y = Input("Enter the second number: ")
    operator = input("Select your required operator from (+, -, *, /): ")

    c = Calculator(x, y)

    if operator == '+':
        print(c.Addition())
    elif operator == '-':
        print(c.Subtraction())
    elif operator == '*':
        print(c.Multiplication())
    elif operator == '/':
        print(c.Division())

    next_calculation = input("Do you want to do another calculation? (yes/no): ").lower()
    if next_calculation == 'no' or next_calculation!='yes':
        break
else:
    print("Invalid Operator")
       
