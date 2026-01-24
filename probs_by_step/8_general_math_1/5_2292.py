n = int(input())

n -= 1

distance = 1

while n > 0:
    round = distance * 6
    
    distance += 1

    n -= round

print(distance)