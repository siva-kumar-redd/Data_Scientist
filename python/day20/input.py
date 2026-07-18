try:
    a = int(input("enter integer"))
    if a == int(a):
        print("valid input")
except ValueError:
    print("invalid input")
else:
    print("program completed")