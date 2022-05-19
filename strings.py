#multiple line string
# from mmap import MADV_NOHUGEPAGE


from calendar import WEDNESDAY


msg = """hello world today 
        we are learning how to use 
        python and vscode.python is fun"""

print(msg)
city = "nairobi"
#upper to convert to uppercase
print(city.upper())
uni = "JKUAT"
print(uni.lower())
fruit = "pineapple"
print(fruit[-1:])
print(fruit[:-1])
#strip removes spaces between the words
f_name = "      michael karanu"
print(f_name.strip())
first_name = "michael"
second_name = "karanu"
full_name = first_name + second_name
print(full_name)
day = WEDNESDAY
print(day.length())