try: 
    with open("customer_data.csv","r") as file:
        file.read()
except FileNotFoundError:
    print("file not found")
else:
    print("Dataset Loaded Successfully")
finally:
    print("Operation Finished")