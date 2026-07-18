age = int(input())
if age<18:
    raise ValueError("age must be greater than 18")
print("eligible")