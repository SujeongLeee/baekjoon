obj_pieces = [1, 1, 2, 2, 2, 8]

current_pieces = [int(x) for x in input().split()]

need_pieces = list()

for i, v in enumerate(current_pieces):
    need_pieces.append(obj_pieces[i] - v)

need_pieces = [str(x) for x in need_pieces]

print(' '.join(need_pieces))