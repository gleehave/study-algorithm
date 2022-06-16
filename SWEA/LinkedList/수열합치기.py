# [수열2]의 첫 숫자보다 큰 숫자를 [수열1]에서 찾아 그 앞에 [수열2]를 끼워넣는다.
# [수열3]의 첫 숫자보다 큰 숫자를 찾아 그 앞에 [수열3]을 끼워넣는다.
# 큰 숫자가 없을 경우, 맨 뒤에 붙인다.
# 마지막 수열까지 합치고 나면, 맨 뒤의 숫자부터 역순으로 10개를 출력한다.

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    S = data.pop(0)

    for i in data:
        for idx, j in enumerate(S):
            if i[0] < j:
                S[idx:idx] = i
                break
        else: # break 가 실행되지 않을 때.
            S.extend(i)

    print("#%d"%test_case, end=" ")
    for i in S[:-11:-1]:
        print(f"{i}", end=' ')
    print()




    # result = data[0]
    # for i in range(M+1):
    #     if i == M:
    #         break
    #
    #     mark = data[i+1][0]
    #     for _ in range(N):
    #         if data[i][_] < mark:
    #             continue
    #         index = _ - 1
    #
    #     result += data[i][:index+1] + data[i+1][:]
    #
    # print("result: ",result)