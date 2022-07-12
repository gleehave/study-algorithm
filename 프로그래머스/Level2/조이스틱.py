# 조이스틱으로 알파벳 이름을 완성하라.

# 상: 다음 알파벳
# 하: 이전 알파벳

# AAA에서 이동한다.
# 좌: 커서 왼쪽 이동 (첫번째 문자에서 이동이면 맨 마지막으로)
# 우: 커서 오른쪽 이동 (마지막 위치에서 오른쪽으로 이동이면 처음으로 이동)

# 만들고자 하는 이름이 name으로 주어질 때, 이름에 대해 조이스틱 조작횟수의 최소를 반환하라.
# 완성해야 하는 이름이 3글자이면 AAA, 4글자이면 AAAA

# name = 'JAZ'
# AAA -> JAA -> JAZ

def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0

    while name[min_move] == "A" and min_move > 0:
        min_move -= 1

    if min_move < 0:
        return answer

    for i, char in enumerate(name):
        answer += min(ord(char)-ord('A'), ord('Z')-ord(char)+1)
        next = i + 1

        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, i+(i+len(name)) - next)
    answer += min_move
    return answer