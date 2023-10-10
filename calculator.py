num1=int(input("enter the first number: "))
op=input("enter the arithmetic operation (+ , - , * , /): ")
num2=int(input("enter the second number: "))
def addition(a,b):
    c=a+b
    print(f"The sum is {c}")
def subtraction(a,b):
    c=a-b
    print(f"The difference is {c}")
def multiplication(a,b):
    c=a*b
    print(f"The product is {c}")
def division(a,b):
    c=a/b
    print(f"the quotient is {c}")
if op=="+":
    addition(num1,num2)
elif op=="-":
    subtraction(num1,num2)
elif op=="*":
    multiplication(num1,num2)
elif op=="/":
    division(num1,num2)
else:
    print("Invalid input")





