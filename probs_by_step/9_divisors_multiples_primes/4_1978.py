n = int(input())

numbers = list(map(int, input().split()))

count = 0

for num in numbers:
    if num == 1:
        continue
    
    divider = 2
    factors = [1]
    while divider <= num / 2 and len(factors) == 1:
        if num % divider == 0:
            factors.append(divider)
        divider += 1
    
    if len(factors) == 1:
        count += 1

print(count)