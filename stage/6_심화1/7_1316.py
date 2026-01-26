n = int(input())
num_group_word = 0

for i in range(n):
    s = input()
    unique_s = len(set(s))
    num_change = 0
    for j in range(len(s)-1):
        if s[j]!=s[j+1]:
            num_change += 1
    if num_change == unique_s-1:
        num_group_word += 1

print(num_group_word)