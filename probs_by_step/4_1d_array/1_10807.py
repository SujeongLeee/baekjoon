n = int(input())

array = input().split()
array = [int(x) for x in array]

v = int(input())

count = 0
for i in array:
    if i == v:
        count += 1
print(count)