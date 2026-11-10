def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: division by zero"
        return a / b
    else:
        return "Error: unknown operator"

def main():
    print("=== Simple Calculator ===")
    while True:
        first = input("\nEnter first number (or 'exit'): ")
        if first.lower() == "exit":
            print("Goodbye!")
            break
        operator = input("Enter operator (+, -, *, /): ")
        second   = input("Enter second number: ")
        result   = calculate(float(first), operator, float(second))
        print(f"Result: {first} {operator} {second} = {result}")

if __name__ == "__main__":
    main()
