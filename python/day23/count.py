def count(n):
    while n<=5:
        yield n
        n += 1


gen = count(1)


for i in gen:
    print(i)