n = int(input())

words = list()
for _ in range(n):
    words.append(input())

count = 0

for word in words:
    appeared = set()

    while len(word) > 0:
        if word[0] in appeared:
            break
        appeared.update(word[0])
        word = word.lstrip(word[0])
    else:
        count += 1
    
print(count)