# 0에서 9까지 숫자가 적힌 N장의 카드가 있다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇장인지 출력하는 프로그램을 만들어라
# 카드 장수가 같은 때는 숫자 값이 큰 것을 출력한다.
from collections import Counter

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input()))
    data.sort(reverse=True)

    result = Counter(data).most_common()

    print('result: ', result)
    print("#{} {} {}".format(test_case, result[0][0], result[0][1]))