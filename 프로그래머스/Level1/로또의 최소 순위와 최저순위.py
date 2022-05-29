def solution(lottos, win_nums):
    # 알아볼 수 없는 번호는 0으로 표기
    # 31, 10, 45, 1, 6, 19
    # 44, 1,  0,  0, 31, 25

    # lottos -> 내가 찍은 번호
    # win_nums -> 당첨번호
    # 당첨 가능한 최고 순위와 최저순위를 배열에 담아서 return

    # 1. 먼저 맞는것부터 찾는다.
    # 2. 맞은 개수 + 0 개수 -> 최고 순위
    # 3. 맞은 개수 - 0 개수 -> 최저 순위

    rank = [6, 6, 5, 4, 3, 2, 1]
    zero_count = lottos.count(0)
    ans = 0
    for i in win_nums:
        if i in lottos:
            ans += 1
    return rank[zero_count + ans], rank[ans]

    # answer = []
    # zero_count = lottos.count(0)
    # count = 0

    #     lottos = sorted(lottos); print('lottos: ', lottos)
    #     win_nums = sorted(win_nums); print('win: ', win_nums)

    #     for integrate in list(zip(lottos, win_nums)):

    #         if integrate[0] == integrate[1]:
    #             count += 1

    #     answer.append(count+zero_count)

    #     if count-zero_count < 0:
    #         answer.append(6)
    #     else:
    #         answer.append(count-zero_count)

    # return answer