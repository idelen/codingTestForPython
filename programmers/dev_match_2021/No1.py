def solution(lottos, win_nums):
    answer = []
    zero_count = 0
    win_count = 0

    for lotto in lottos:
        if lotto == 0:
            zero_count += 1
        else:
            for win_num in win_nums:
                if lotto == win_num:
                    win_count += 1
                    break

    if zero_count == 6:
        answer = [1, 6]
    elif win_count == 6:
        answer = [1, 1]
    else:
        min_rank = (7 - win_count) if (7 - win_count) <= 6 else 6
        total_count = win_count + zero_count
        max_rank = (7 - total_count) if (7 - total_count) <= 6 else 6
        answer = [max_rank, min_rank]

    return answer


lottos_list = [[44, 1, 0, 0, 31, 25], [0, 0, 0, 0, 0, 0], [45, 4, 35, 20, 3, 9]]
win_nums_list = [[31, 10, 45, 1, 6, 19], [38, 19, 20, 40, 15, 25], [20, 9, 3, 45, 4, 35]]

for i in range(3):
    print(solution(lottos_list[i], win_nums_list[i]))
