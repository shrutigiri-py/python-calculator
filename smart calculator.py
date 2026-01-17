# a smart calculator
def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return "Cannot divide by zero" if b == 0 else a / b
    else:
        return "Invalid operation"
    
print("🌟 Welcome to Smart Calculator 🌟")
result = float(input("Enter first number: "))

while True:
    op = input("Enter operation (+, -, *, /) or press = to stop :")
    if op == "=":
        print(result)
        break

    num = float(input("Enter next number: "))
    new_result = calculate(result, op, num)
    # isinstance help check the type of data
    if isinstance(new_result, str):
        print(new_result)
        break

    result = new_result
    print("Current Result:", result)











   