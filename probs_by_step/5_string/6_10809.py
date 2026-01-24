S = input()

place = list()

for i in range(97, 123):
    try:
        place.append(S.index(chr(i)))
    except:
        place.append(-1)

print(' '.join(map(str, place)))