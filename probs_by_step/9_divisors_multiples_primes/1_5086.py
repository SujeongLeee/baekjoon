terminated = False

while not terminated:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0: # check terminated
        terminated = True
        break

    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')