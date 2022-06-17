# str1, str2
# str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고,
# 그 중에 많은 글자의 개수를 출력하는 프로그램 만들어라.

T = int(input())

for test_case in range(1, T + 1):
    str1 = set(str(input()))
    str2 = str(input())

    count = {}

    for value in str1:
        count[value] = 0

    for Alphabet in str2:
        if Alphabet in count:
            count[Alphabet] += 1
    print("#{} {}".format(test_case, str(max(count.values()))))