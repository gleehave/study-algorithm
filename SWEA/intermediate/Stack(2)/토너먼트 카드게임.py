# 가위바위보 카드를 이용해 토너먼트로 1명을 뽑느다.
# 1~N 까지 N명의 학생이 N장의 카드를 나눠갖는다.
# 전체를 2개의 그룹으로 나누고, 그룹의 상자끼리 카드를 비교해서 이긴 사람이 최종 승자
# 만약 같은 카드의 경우, 번호가 작은 쪽을 승자로 한다.

# 그룹 1: i ~ (i+j)//2
# 그룹 2: (i+j)//2+1 ~ j
# 1 : 가위
# 2 : 바위
# 3 : 보

def rsp(a, b):
    if data[a] == data[b]:
        return a
    elif data[a] - data[b] == 1 or data[a]-data[b]==-2:
        return a
    return b

def divide(start, end):
    if start == end:
        return start
    a = divide(start, (start+end)//2)
    b = divide((start+end)//2+1, end)
    return rsp(a, b)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    result = divide(0, N-1) + 1

    print("#{} {}".format(test_case, result))


