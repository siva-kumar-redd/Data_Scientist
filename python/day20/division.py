from decimal import DivisionByZero
try:
    num1,num2 = map(int,input().split())
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    print(num1/num2)
except DivisionByZero:
    print("number 0 cannot be divided")