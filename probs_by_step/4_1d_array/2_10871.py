n, x = map(int, input().split())

array = input().split()
array = [int(i) for i in array]

output = str()

for i in array:
    if i < x:
        output += f"{i} "

output = output[:-1]

print(output)