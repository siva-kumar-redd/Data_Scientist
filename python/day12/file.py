try:
    with open("AI.txt","r") as file:
        file.read()
except FileNotFoundError:
    print("file not found")
finally:
    print("file processing")