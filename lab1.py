print("Good  morning!\n")
print("---- Simple Calculator ----")
op = ''
while op != 'q':
    print("Print q to exit")
    op = input("Operation (+ - * /): ")
    if op == 'q':
        continue
    if op in ('+', '-', '*', '/'):
        try:
            x = float(input("x = "))
            y = float(input("y = "))
        except ValueError:
            print("Not a number")
            continue 
        if op == '+':
            print(f"{x} + {y} = {x + y}")
        elif op == '-':
            print(f"{x} - {y} = {x - y}")
        elif op == '*':
            print(f"{x} * {y} = {x * y}")
        elif op == '/':
            if y != 0:
                print(f"{x} / {y} = {x / y}")
            else:
                print("Division by zero")
    else:
        print("Wrong operation")

 

