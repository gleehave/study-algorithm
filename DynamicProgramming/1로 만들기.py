# 정수 x 가 주어진다.
# 1. x가 5로 나누어 떨어지면, 5로 나눈다.
# 2. x가 3으로 나누어 떨어지면, 3으로 나눈다.
# 3. x가 2로 나누어 떨어지면, 2로sksnsek.
# 4. x에서 1을 뺀다.

# 정수 x가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다.
# 최소 연산 횟수를 구해라

x = int(input())
d = [0]*50
for i in range(2, x+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)
    print('d: ', d)

print(d[x])