a = int(input())
b = int(input())

oneth = b % 10
tenth = ((b % 100) - oneth) // 10
hundredth = (b - tenth - oneth) // 100

print(a * oneth)
print(a * tenth)
print(a * hundredth)
print(a * b)