# n명이 줄을 서서 기다림.
# 각 심사하는 장소마다 소요되는 시간이 다르다.

# 처음에는 모든 심사대가 비어있다.
# 1개의 심사대는 1명만 심사.

# 가장 앞에서 있는 사람은 비어 있는 심사대로 받는다.
# 하지만, 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수 있다.

# n = 사람수
# times = 시간이 담긴 배열

def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left+right) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid -1
        elif people < n:
            left = mid + 1
    return answer