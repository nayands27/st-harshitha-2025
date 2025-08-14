def add(x, y):
    c = x+y
    return c

def sub(x, y):
    c = x-y
    return c

def mul(x, y):
    c = x*y
    return c

def div(x, y):
    c = x//y
    return c

num1 = int(input("Enter first value: "))
num2 = int(input("Enter 2nd value: "))

op = input("for adddition enter-1|for Subtraction enter-2 |for Multiplication enter-3|for Division enter-4: ")

if op == '1':
    result = add(num1, num2)
    print(f"Output : {result}")
elif op == '2':
    result = sub(num1,num2)
    print(f"Output : {result}")
elif op == '3':
    result = mul(num1, num2)
    print(f"Output : {result}")
elif op == '4':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
       result = num1 / num2
       print(f"Result: {num1} / {num2} = {result}")
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
    
    
