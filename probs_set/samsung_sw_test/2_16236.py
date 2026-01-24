# None, try-except, BFS

n = int(input())

space = []
for i in range(n):
    space.append(list(map(int, input().split())))


# 비어있지 않은 공간의 숫자별 좌표 구하기
def find_non_zeroes(space):
    non_zeroes = {}
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j] != 0:
                if space[i][j] in non_zeroes.keys():
                    non_zeroes[space[i][j]].append([i, j])
                else:
                    non_zeroes[space[i][j]] = [[i, j]]
    return non_zeroes

# target의 index 구하기
def find_index(space, target):
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j] == target:
                return [i, j]

# 지나갈 수 있는 길 찾기
def find_available(space, size):
    for i in range(len(space)):
        for j in range(len(space[i])):
            # 지나갈 수 있으면 1, 아니면 0
            if space[i][j] <= size:
                space[i][j] = 1
            else:
                space[i][j] = 0
    return space

# start index -> finish index 가장 짧은 시간 구하기 (BFS)
def calculate_shortest_time(available, start, finish):
    searched = []
    depth = 0
    need_search = {depth: [start]}
    need_search[depth + 1] = []

    while need_search != []:
        # Goal Check
        current_search = need_search[depth][0]
        if current_search == finish:
            return depth
        searched.append(current_search)

        if current_search[0] == 0:
            # (0, 0)
            if current_search[1] == 0:
                # right
                if available[current_search[0]][current_search[1] + 1] != 0:
                    if [current_search[0], current_search[1] + 1] not in searched:
                        if [current_search[0], current_search[1] + 1] not in need_search[depth] + need_search[depth + 1]:
                            need_search[depth + 1].append([current_search[0], current_search[1] + 1])
            # (0, n - 1)
            elif current_search[1] == n - 1:
                # left
                if available[current_search[0]][current_search[1] - 1] != 0:
                    if [current_search[0], current_search[1] - 1] not in searched:
                        if [current_search[0], current_search[1] - 1] not in need_search[depth] + need_search[depth + 1]:
                            need_search[depth + 1].append([current_search[0], current_search[1] - 1])
            # (0, ~)
            else:
                # right & left
                if available[current_search[0]][current_search[1] + 1] != 0:
                    if [current_search[0], current_search[1] + 1] not in searched:
                        if [current_search[0], current_search[1] + 1] not in need_search[depth] + need_search[depth + 1]:
                            need_search[depth + 1].append([current_search[0], current_search[1] + 1])
                if available[current_search[0]][current_search[1] - 1] != 0:
                    if [current_search[0], current_search[1] - 1] not in searched:
                        if [current_search[0], current_search[1] - 1] not in need_search[depth] + need_search[depth + 1]:
                            need_search[depth + 1].append([current_search[0], current_search[1] - 1])
            # down
            if available[current_search[0] + 1][current_search[1]] != 0:
                if [current_search[0] + 1, current_search[1]] not in searched:
                    if [current_search[0] + 1, current_search[1]] not in need_search[depth] + need_search[depth + 1]:
                        need_search[depth + 1].append([current_search[0] + 1, current_search[1]])
        elif current_search[0] == n - 1:
            # (n - 1, 0)
            if current_search[1] == 0:
                # right
                if available[current_search[0]][current_search[1] + 1] != 0:
                    if [current_search[0], current_search[1] + 1] not in searched:
                        if [current_search[0], current_search[1] + 1] not in need_search[depth] + need_search[depth + 1]:
                            need_search[depth + 1].append([current_search[0], current_search[1] + 1])
            # (n - 1, n - 1)
            elif current_search[1] == n - 1:
                # left
                if available[current_search[0]][current_search[1] - 1] != 0:
                    if [current_search[0], current_search[1] - 1] not in searched:
                        if [current_search[0], current_search[1] - 1] not in need_search[depth] + need_search[depth + 1]:
                            need_search[depth + 1].append([current_search[0], current_search[1] - 1])
            # (n - 1, ~)
            else:
                # right & left
                if available[current_search[0]][current_search[1] + 1] != 0:
                    if [current_search[0], current_search[1] + 1] not in searched:
                        if [current_search[0], current_search[1] + 1] not in need_search[depth] + need_search[depth + 1]:
                            need_search[depth + 1].append([current_search[0], current_search[1] + 1])
                if available[current_search[0]][current_search[1] - 1] != 0:
                    if [current_search[0], current_search[1] - 1] not in searched:
                        if [current_search[0], current_search[1] - 1] not in need_search[depth] + need_search[depth + 1]:
                            need_search[depth + 1].append([current_search[0], current_search[1] - 1])
            # up
            if available[current_search[0] - 1][current_search[1]] != 0:
                if [current_search[0] - 1, current_search[1]] not in searched:
                    if [current_search[0] - 1, current_search[1]] not in need_search[depth] + need_search[depth + 1]:
                        need_search[depth + 1].append([current_search[0] - 1, current_search[1]])
        else:
            # (~, 0)
            if current_search[1] == 0:
                # right
                if available[current_search[0]][current_search[1] + 1] != 0:
                    if [current_search[0], current_search[1] + 1] not in searched:
                        if [current_search[0], current_search[1] + 1] not in need_search[depth] + need_search[depth + 1]:
                            need_search[depth + 1].append([current_search[0], current_search[1] + 1])
            # (~, n - 1)
            elif current_search[1] == n - 1:
                # left
                if available[current_search[0]][current_search[1] - 1] != 0:
                    if [current_search[0], current_search[1] - 1] not in searched:
                        if [current_search[0], current_search[1] - 1] not in need_search[depth] + need_search[depth + 1]:
                            need_search[depth + 1].append([current_search[0], current_search[1] - 1])
            # (~, ~)
            else:
                # right & left
                if available[current_search[0]][current_search[1] + 1] != 0:
                    if [current_search[0], current_search[1] + 1] not in searched:
                        if [current_search[0], current_search[1] + 1] not in need_search[depth] + need_search[depth + 1]:
                            need_search[depth + 1].append([current_search[0], current_search[1] + 1])
                if available[current_search[0]][current_search[1] - 1] != 0:
                    if [current_search[0], current_search[1] - 1] not in searched:
                        if [current_search[0], current_search[1] - 1] not in need_search[depth] + need_search[depth + 1]:
                            need_search[depth + 1].append([current_search[0], current_search[1] - 1])
            # down & up
            if available[current_search[0] + 1][current_search[1]] != 0:
                if [current_search[0] + 1, current_search[1]] not in searched:
                    if [current_search[0] + 1, current_search[1]] not in need_search[depth] + need_search[depth + 1]:
                        need_search[depth + 1].append([current_search[0] + 1, current_search[1]])
            if available[current_search[0] - 1][current_search[1]] != 0:
                if [current_search[0] - 1, current_search[1]] not in searched:
                    if [current_search[0] - 1, current_search[1]] not in need_search[depth] + need_search[depth + 1]:
                        need_search[depth + 1].append([current_search[0] - 1, current_search[1]])
        
        need_search[depth].remove(current_search)

        # depth update
        if need_search[depth] == []:
            depth += 1
            need_search[depth + 1] = []

time = 0
size = 2
feed_count = 0
non_zeroes = find_non_zeroes(space)

# 먹을 수 있는 게 남아있다면
while min(non_zeroes.keys()) < size:
    # 먹이로 이동
    shark_index = find_index(space, 9)
    
    available = find_available(space, size)


    ## 어떻게 다음 타겟 결정하지
    target_indices = []
    distances = []

    for i in non_zeroes:
        if i < size:
            for j in non_zeroes[i]:
                target_indices.append(j)
                distances.append(calculate_shortest_time(available, shark_index, j))


    print(shark_index)
    print(non_zeroes)
    print(target_index)
    #print(target_index)
    time += calculate_shortest_time(available, shark_index, target_index)
    space[target_index[0]][target_index[1]] = 9
    space[shark_index[0]][shark_index[1]] = 0
    print(space)
    feed_count += 1

    # size 키우기
    if feed_count == size:
        feed_count = 0
        size += 1
    
    # non_zeroes 초기화
    non_zeroes = find_non_zeroes(space)


print(time)