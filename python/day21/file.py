try:
    with open("abc.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    raise FileNotFoundError("file not found")