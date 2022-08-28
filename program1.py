class cal():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation(add,sub,mult,div): ")
obj = cal(a, b)
if op == "add":
    print("Result: ", obj.add())
elif op == "sub":
    print("Result: ", obj.sub())
elif op == "mult":
    print("Result: ", obj.mul())
elif op == "div":
    print("Result: ", obj.div())
else:
    print("Invalid operation!!")