
try:
    subjects = int(input("enter no of subjects"))

    cal = 500/subjects
    print(cal)
except ZeroDivisionError:
    print("cannot be divided by zero")
except ValueError:
    print("enter only numbers")