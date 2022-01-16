# 숫자가 쓰인 카드들이 nxm 형태로 있다. n은 행의 개수, m은 열의 개수이다.
# 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 선택된 행에서 가장 낮은 카드를 뽑는다.
# 처음에 카드를 골라낼 행을 선택할 때,
# 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세운다.

n,m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)