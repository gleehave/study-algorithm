# N개의 수열이 주어진다.
# M개의 숫자를 지정된 위치에 추가하면 완성된다.
# 완성된 수열에서 인덱스 L의 데이터를 출력하라.

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    data = list(map(int, input().split()))
    requirements=[]
    for _ in range(M):
        requirements.append(list(map(int, input().split())))

    for requirement in requirements:
        temp = data[:requirement[0]]
        temp.append(requirement[1])
        data = temp + data[requirement[0]:]

    print("#{} {}".format(test_case, data[L]))