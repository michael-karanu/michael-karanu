try:
    div = 10/0
    value = int(input("enter a number "))
    print(value)
except ValueError:
    print("invalid number")
except ZeroDivisionError:
    print("divided by zero")        