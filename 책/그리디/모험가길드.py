# 모험가 N명이 있다.
# '공포도'는 x 이다.
# 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 있어야 여행을 할 수 있다.

# 최대 몇개의 그룹을 만들 수 있는가?

# N = 5
# 공포도: 2 3 1 2 2
# 결과: 2   (그룹1: 1 / 그룹2: 2 2/ 나머지 2와 3은 여행을 떠나지 못한다.)

N = int(input())
data = sorted(list(map(int, input().split()))) # 1 2 2 2 3

result = 0
count = 0
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)