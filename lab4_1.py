statement = ""

def calculate(a, b, operator):
    if operator == "+":
        return 0, a + b
    if operator == "-":
        return 0, a - b
    if operator == "*":
        return 0, a * b
    if operator == "/":
        try:
            return 0, a / b
        except:
            return 1, "Error: division by zero is not allowed"
    if operator == "%":
        try:
            return 0, a % b
        except:
            return 1, "Error: Modulus by zero is not allowed"
    
    else:
        return 2, "Error: operator is not valid"
    
while statement.upper() != "NO":
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /, %): ")
    err, res = calculate(num_1, num_2, operator)
    if err == 1:
        print(res)
        continue
    if err == 2:
        print(res)
    if not err:
        print(f"{res:.1f}")
    statement = input("Please enter YES to continue or NO to stop ")


print("The end, thank you")

