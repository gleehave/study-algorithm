def correct(s):
    stack = []
    for value in s:
        if value == '[' or value == '{' or value == '(':
            stack.append(value)
        elif value == ']' or value == '}' or value == ')':
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True


def solution(s):
    count = 0
    s = list(s)
    x = len(s)

    for _ in range(x):
        temp = s.pop(0)
        s.append(temp)

        if correct(s):
            count += 1

    return count

s = "[)(]"
print(solution(s))