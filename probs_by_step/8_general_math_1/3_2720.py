t = int(input())

units = [25, 10, 5, 1]

for _ in range(t):
    change = int(input())
    coins = list()

    for unit in units:
        coins.append(change // unit)
        change -= unit * coins[-1]
    
    coins = [str(x) for x in coins]

    print(' '.join(coins))