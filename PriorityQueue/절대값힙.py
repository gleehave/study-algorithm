# x != 0 이면, 배열에 x를 추가한다.
# x = 0 이면, 배열에서 절대값이 가장 각은 값을 출력하고, 배열에서 제거한다.

N = int(input())
arr = []
queue_plus = []
queue_minus = []

for _ in range(N):
    data = int(input())
    arr.append(data)

for i in range(N):
    if arr[i] != 0:
        if arr[i] > 0:
            queue_plus.append(arr[i])
        else:
            queue_minus.append(arr[i])
    elif arr[i] == 0:
        