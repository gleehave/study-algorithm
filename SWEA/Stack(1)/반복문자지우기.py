# C,A,A,A,B,B,A
# C,A,B,B,A
# C,A,A
# C -> 문자열 길이 1


T = int(input())
for test_case in range(1, T + 1):
    data = list(input())
    compare = []

    while data:
        if not compare:
            compare.append(data.pop(0))

        if compare[-1] == data[0]:
            compare.pop(-1)
            data.pop(0)
            continue

        compare.append(data.pop(0))

    print("#{} {}".format(test_case, len(compare)))
