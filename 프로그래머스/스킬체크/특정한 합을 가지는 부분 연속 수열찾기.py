# N개의 자연수로 구성된 수열
# 합이 M이 부분 연속 수열의 개수를 알고 싶다.

n = 5
m = 5
data = [1,2,3,4,5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1

    interval_sum -= data[start]