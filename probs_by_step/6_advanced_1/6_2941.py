cr_chars = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
count = 0

while len(word) > 0:
    for cr_char in cr_chars:
        if word[:len(cr_char)] == cr_char:
            count += 1
            word = word[len(cr_char):]
            break
    else:
        count += 1
        word = word[1:]

print(count)