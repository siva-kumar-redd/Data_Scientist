def sample():
    yield 1
    yield 2
    yield 3

gen = sample()
print(next(gen))
print(next(gen))
print(next(gen))
