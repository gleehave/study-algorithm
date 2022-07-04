# ()() 혹은 (())() 은 올바른 괄호
# 올바른 괄호이면 True, 그렇지 않으면 False를 return 하라.

s = "(()("

def solution(s):
    N = len(s)
    stack = []
    for index in range(N):
        if s[index] == '(':
            stack.append(s[index])
        elif s[index] == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if stack:
        return False
    return True

print(solution(s))