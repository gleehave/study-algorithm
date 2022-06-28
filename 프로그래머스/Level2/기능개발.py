# 각 기능은 100% 일때, 반영할 수 있다.
# 개발속도는 모두 다르므로, 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
# 이때, 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포된다.

# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses
# 작업의 개발 속도가 적힌 정수배열 speeds가 주어진다.

# 각 배포마다 몇 개의 기능이 배포되는가?

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
# 93% 기능은 7일 / 30% 기능은 3일(2.x일) -> 93%가 먼저이므로, 7일째에 2개를 배포한다.
# 55% 기능은 9일, 9일째에 1개를 배포한다.
# return [2, 1]

import math

def solution(progresses, speeds):
    date = []
    result = []
    for i in range(len(progresses)):
        date.append(math.ceil(((100 - progresses[i]) / speeds[i])))

    while date:
        count = 1
        ready = date.pop(0)
        for next in date:
            if ready >= next:
                count += 1
            else:
                break
        for _ in range(count-1):
            date.pop(0)
        result.append(count)
    return result

solution(progresses, speeds)