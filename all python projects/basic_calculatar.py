def add(a,b):
    answer = a+b
    print(answer)
def sub(a,b):
    answer = a-b
    print(answer)
def mul(a,b):
    answer = a*b
    print(answer)
def div(a,b):
    answer = a/b
    print(answer)

while True:
    print("a: for addition")
    print("b: for sub")
    print("c: for maltification")
    print("d: for divion")
    chose = input("chose the option : ")
    if chose == "a":
        a = int(input("enter number : "))
        b = int(input("enter number : "))
        add(a,b)
    elif chose == "b":
        a = int(input("enter number : "))
        b = int(input("enter number : "))
        sub(a,b)
    elif chose == "c":
        a = int(input("enter number : "))
        b = int(input("enter number : "))
        mul(a,b)
    elif chose == "d":
        a = int(input("enter number : "))
        b = int(input("enter number : "))
        div(a,b)
    else:
        break