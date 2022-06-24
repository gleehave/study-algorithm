# 0과 1로 이루어진 문자열 S가 주어진다.
# S의 모든 숫자를 전부 동일하게 만들려고 한다.
# S에서 연속된 1개 이상의 숫자를 잡고 모두 뒤집는다.

# S = 0001100
    # 전체를 뒤집는다. -> 1110011
    # 4번째 부터 5번째 문자까지 뒤집으면 1111111이 된다.
    # 2번만에 같은 숫자로 만든다.

data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

