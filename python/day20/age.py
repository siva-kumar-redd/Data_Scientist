try:
    age = int(input())
    if age>=18:
        print(age)
except ValueError:
    print("age is should only numbers")