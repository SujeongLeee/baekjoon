word = input()

is_palidrome = 1

for i in range(len(word)):
    if word[i] != word[- (i + 1)]:
        is_palidrome = 0

print(is_palidrome)