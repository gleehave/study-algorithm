# N 개의 숫자로 이루어진 수열이 주어진다.
# 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 한다.
# 수열의 맨 앞에 있는 숫자를 출력하는 프로그램

import queue

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    for _ in range(M):
        temp = data.pop(0)
        data.append(temp)

    print("#{} {}".format(test_case, data[0]))


'''
from collections import deque

T = int(input())
for tc in range(1, T+1):
    n , m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    
    cnt = 0
    while cnt < m:
        q.append(q.popleft())
        cnt += 1
    print("#{} {}".format(tc, q.popleft()))

'''


