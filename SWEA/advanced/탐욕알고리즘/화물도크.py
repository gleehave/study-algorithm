# 0시부터 다음날 0시 까지
# 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
# 최대 몇 대의 화물차가 이용할 수 있는가?

# 신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고,
# 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.

# 예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다

# 5
# 20 23
# 17 20
# 23 24
# 4 14
# 8 18

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]
    schedule = sorted(schedule, key=lambda x: x[1])
    print(schedule)
    available = 0

    now = 0
    for i in range(N):
        start = schedule[i][0]
        end = schedule[i][1]

        if now <= start:
            available += 1
            now = end

    print("#{} {}".format(test_case, available))

