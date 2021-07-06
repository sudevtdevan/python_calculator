# Program to make a calculator
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def modulo(x,y):
    return x % y 
def square(x):
    return x*x       
print("SELECT THE ARITHMETIC OPERATION")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.MODULUS")
print("6.SQUARE")
while True:
    choice=input("ENTER YOUR CHOICE (1/2/3/4/5/6): ")
    if choice in ('1','2','3','4','5'):
        a=int(input("ENTER THE FIRST NUMBER: "))
        b=int(input("ENTER THE SECOND NUMBER: "))
        if choice=='1':
            print(a,"+",b,"=",add(a, b))
        elif choice=='2':
            print(a,"-",b,"=",subtract(a,b))
        elif choice=='3':
            print(a,"*",b,"=",multiply(a,b))
        elif choice=='4':
            print(a,"/",b,"=",divide(a,b))
        elif choice == '5':
            print(a,"%",b,"=",modulo(a,b))    
        break
    if choice in ('6'):
        a=int(input("ENTER THE NUMBER: "))    
        if choice=='6':
            print(a,"^2","=",square(a))    
        break
    else:
        print("INVALID INPUT")