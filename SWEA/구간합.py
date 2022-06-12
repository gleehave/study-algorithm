# N개의 정수가 들어있는 배열
# 이웃한 M개의 합을 계산
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    result = []

    for i in range(0,N-M+1):
        result.append(sum(data[i:i+M]))
        print('data: ',data[i:i+M])
    print('result: ',result)
    print("#{} {}".format(test_case,max(result)-min(result)))
