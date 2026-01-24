lengths = sorted(list(map(int, input().split())))

if lengths[2] >= lengths[0] + lengths[1]:
    lengths[2] = lengths[0] + lengths[1] - 1

print(sum(lengths))