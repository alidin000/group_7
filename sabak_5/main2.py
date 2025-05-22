# mini calculator

san1 = input("birinchi san:")
san2 = input("ekinchi san:")
operation = input("оперцияны танда(+,-,*,/):")

try:
    san1 = int(san1)
    san2 = int(san2)
except ValueError as e:
    raise ValueError("Бизге сан керек!!!")

if operation == '+':
    print(f"a+b = {san1+san2}")
elif operation == '-':
    print(f"a-b = {san1-san2}")
elif operation == '*':
    print(f"a*b = {san1*san2}")
elif operation == '/':
    if san2 == 0:
        raise ZeroDivisionError("экинчи сан 0 боло албайт")
    else:
        print(f"a/b = {san1/san2}")