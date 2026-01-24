word = input().upper()

char_set = set(x for x in word)

char_counts = dict()

for i in char_set:
    count = 0
    for j in word:
        if i == j:
            count += 1
    char_counts[i] = count

max_char = max(char_counts, key = char_counts.get)
max_val = char_counts[max_char]
if len(char_set) > 1:
    del(char_counts[max_char])

    second_char = max(char_counts, key = char_counts.get)
    second_val = char_counts[second_char]

    if max_val > second_val:
        print(max_char)
    else:
        print("?")
else:
    print(max_char)