try:
    num_1 = int(input("enter first number :"))
    op = input("enter operation :")
    num_2 = int(input("enter second number :"))        
    if op == "+":
        print("addition is :",num_1 + num_2)
    elif op == "-":
        print("subtraction is :",num_1 - num_2)
    elif op == "*":
        print("multiplication is :",num_1 * num_2)
    elif op == "/":
        print("division is :",num_1 / num_2)
except ValueError:
    print("invalid value")
except ZeroDivisionError:
    print("divided by zero") 