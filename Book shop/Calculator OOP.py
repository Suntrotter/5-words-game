class Calculator(object):
    def __init__(self, arg1, operator, arg2):
        self.arg1 = arg1
        self.operator = operator
        self.arg2 = arg2

    def add(self, arg1, arg2):
        return self.arg1 + self.arg2

    def subtract(self, arg1, arg2):
        return self.arg1 - self.arg2

    def multiply(self, arg1, arg2):
        return self.arg1 * self.arg2

    def divide(self, arg1, arg2):
        return self.arg1 / self.arg2


arg1 = int(input("Please enter the first figure: "))
operator = input("Please enter + - * / : ")
arg2 = int(input("Please enter the second figure: "))

if __name__ == '__main__':
    c = Calculator(arg1, operator, arg2)
    if operator == "+":
        print(arg1, operator, arg2, "=", c.add(arg1, arg2))
    elif operator == "-":
        print(arg1, operator, arg2, "=", c.subtract(arg1, arg2))
    elif operator == "*":
        print(arg1, operator, arg2, "=", c.multiply(arg1, arg2))
    elif operator == "/":
        print(arg1, operator, arg2, "=", c.divide(arg1, arg2))
    else:
        print("Wrong operator!")


