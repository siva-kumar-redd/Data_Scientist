text = "Python"

word = {}

for i in text:
    word[i] = word.get(i,0)+1
print(word)