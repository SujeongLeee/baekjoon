def prize_calculator(result_input):
    a, b, c = map(int, result_input.split())
    result = [a, b, c]
    result.sort()

    if max(result) == min(result):
        prize = result[0] * 1000 + 10000
    else:
        if (result[0] == result[1]) or (result[1] == result[2]):
            prize = result[1] * 100 + 1000
        else:
            prize = max(result) * 100
    
    return prize

print(prize_calculator(input()))