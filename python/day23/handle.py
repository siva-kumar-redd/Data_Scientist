numbers = [1]

it = iter(numbers)

try:
    while True:
        print(next(it))
except StopIteration:
    print("Iteration completed.")