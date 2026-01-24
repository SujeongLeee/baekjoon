array = []

for _ in range(10):
    array.append(int(input()))

remainders = []
for i in array:
    remainders.append(i % 42)

remainders = set(remainders)

print(len(remainders))