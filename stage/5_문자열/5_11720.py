count = int(input())
numbers = str(input())

a=0
for i in range(count):
    a += int(numbers[i])
print(a)


# sum = 0
# q = numbers

# for i in range(len(str(numbers))):
#     sum += q % (10**(i+1)) / (10**i)
#     q -= q % (10**(i+1))

# print(int(sum))