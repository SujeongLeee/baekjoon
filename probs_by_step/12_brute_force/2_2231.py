n = int(input())

possible_min = max(n - len(str(n)) * 9, 0)

def cal_digit_sum(n):
    sum = 0
    for i in range(len(str(n))):
        sum += int(str(n)[i])
    return sum

for i in range(possible_min, n):
    if i + cal_digit_sum(i) == n:
        print(i)
        break
else:
    print(0)