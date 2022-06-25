# 실패율: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
# 전체 스테이지의 개수 N
# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때,
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨 있는 배열을 return

# 스테이지에 도달한 유저가 없는 경우, 해당 스테이지의 실패율은 0으로 한다.
# 만약 실패율이 같다면 작은 번호의 스테이지가 먼저 오도록 한다.

# N: 5 | stages = [2,1,2,6,2,4,3,3] | result = [3,4,1,5]
# 1번 스테이지에는 총 8명의 사용자가 도전, 이 중 1명의 사용자가 클리어하지 못했다. 실패율 1/8
# 2번 스테이지에는 총 7명의 사용자가 도전, 이 중 3명의 사용자가 클리어하지 못했다. 실패율 3/7

# N = int(input())
# stages = sorted([2, 1, 2, 6, 2, 4, 3, 3]) # 1 2 2 2 3 3 4 6
# unique = set(stages)
# user = len(stages)
# fail = []
#
# while True:
#     for stage in unique:
#         stay = stages.count(stage)
#         fail.append(stay/(user-stay))
#         user -= stay
#         if user <= 0:
#
#     break
# result = zip(stages, fail)
#
# for _ in result:
#     print(_)

N = int(input())
stages = sorted([2, 1, 2, 6, 2, 4, 3, 3]) # 1 2 2 2 3 3 4 6

def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N+1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    return answer

print(solution(N, stages))