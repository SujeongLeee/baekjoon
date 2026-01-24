a, b, v = map(int, input().split())

day = (v - a) // (a - b)

if (v - a) % (a - b) == 0:
    day += 1
else:
    day += 2

print(day)

"""

a, b, v = map(int, input().split())

day = 1
pos = 0
goal_reached = False

while not goal_reached:
    pos += a
    if pos >= v:
        goal_reached = True
        break
    
    pos -= b
    day += 1

print(day)

"""