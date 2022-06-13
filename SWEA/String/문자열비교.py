# str1, str2
# str2안에 str1과 일치하는 부분을 찾는 프로그램
# 존재하면 1, 그렇지 않으면 0

T = int(input())
for test_case in range(1, T + 1):
    str1 = str(input())
    str2 = str(input())

    result = 0

    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            result = 1
    print("#{} {}".format(test_case, result))