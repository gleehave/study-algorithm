# 어떤 수 n 이 1이 될때까지 다음의 2과정 중 1개를 반복적으로 수행한다.
# 1. n에서 1을 뺀다.
# 2. n을 k로 나눈다.
# 예를 들어, n=17, k=4라고 할 때, 1번 과정을 수행하면 n은 16이 된다.
# 이후에 2번의 과정을 수행하면 n은 1이 된다.

n, k = map(int, input().split())
result = 0

# n이 k 이상이라면 k로 계속 나누기
while n >= k:
    # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

# 마지막으로 남은 수에 대해서 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)