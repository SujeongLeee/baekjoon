word = input()

time = 0

for char in word:
    char_num = ord(char) - ord("A")
    if char_num <= 14:
        time += char_num // 3 + 3
    elif char_num <= 18:
        time += 8
    elif char_num <= 21:
        time += 9
    else:
        time += 10

print(time)