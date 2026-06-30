try:
    num = int(input())

except ValueError:
    print("enter numbers only")


finally:
    print("Calculation successful")