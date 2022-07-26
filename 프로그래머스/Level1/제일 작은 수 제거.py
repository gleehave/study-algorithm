# arr에서 가장 작은 수를 제거한 배열을 리턴해라.
# 단, 리턴하려는 배열이 빈 배열인 경우, 베열에 -1을 채워 리턴한다.

arr = [4,3,2,1]

def solution(arr):
    min_index = arr.index(min(arr))
    arr.remove(arr[min_index])

    if len(arr) == 0:
        return [-1]
    return arr

print(solution(arr))