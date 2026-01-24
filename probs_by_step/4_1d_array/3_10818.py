n = int(input())

array = input().split()
array = [int(x) for x in array]

min = array[0]
max = array[0]

for i in array:
    if i < min:
        min = i
    elif i > max:
        max = i

print(min, max)