# 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을
# m 번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스에 해당하는 수는 k번을 초과하여 더해질 수 없다.

# 5 8 3
# 2 4 5 4 6
# result: 46

# N,M,K f를 공백으로 구분하여 입력받기
n,m,k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort()  # 2 4 4 5 6
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break

    result += second
    m -= 1

print(result)