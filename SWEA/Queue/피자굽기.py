# N개의 피자를 동시에 구울 수 있는 화덕이 있다.
# 1~M번 까지의 M개의 피자를 순서대로 화덕에 넣는다.
# 치즈의 양에 따라 녹는 시간이 다르므로, 꺼내지는 순서는 바뀔 수 있다.

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    pizza_num = [i for i in range(M)]
    queue = pizza_num[0:N]
    while len(queue) != 1:
        if cheese[queue[0]] != 1:
            cheese[queue[0]] = cheese[queue[0]] // 2
            queue.append(queue.pop(0))
        else:
            queue.pop(0)
            if N != M:
                queue.append(pizza_num[N])
                N += 1

    print('#{} {}'.format(test_case, queue[0] + 1))