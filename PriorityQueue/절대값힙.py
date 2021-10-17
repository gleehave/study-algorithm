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
        elif arr[i] < 0:
            queue_minus.append(arr[i])
    elif arr[i] == 0:

        if not queue_minus and not queue_plus:
            print(0)
            continue
        queue_minus.sort(reverse=True)
        queue_plus.sort()
        print('minus:', queue_minus)
        print('plus: ', queue_plus)
        if not queue_minus:
            print(queue_plus.pop(0))
            continue
        if not queue_plus:
            print(queue_minus.pop(0))
            continue
        if min(queue_plus) == abs(max(queue_minus)):
            print(queue_minus.pop(0))
            continue
        elif min(queue_plus) != abs(max(queue_minus)):
            print(queue_plus.pop(0))      
            continue