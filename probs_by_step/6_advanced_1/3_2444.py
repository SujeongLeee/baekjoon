n = int(input())

for i in range(1, 2 * n - 1 + 1):
    print((' ' * abs(n - i)) + ('*' * min(2 * i - 1, - 2 * i + 4 * n - 1)))