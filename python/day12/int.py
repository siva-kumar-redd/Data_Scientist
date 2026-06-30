try:
    number = int(input())
    print(100/number)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("enter valid numbers")