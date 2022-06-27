# n개의 음이 아닌 정수들이 있다.
# 이 정수들의 순서를 바꾸지 않고, 적절히 더하거나 빼서 타겟넘버를 만든다.

# [1,1,1,1,1]로 3을 만들려면, 5가지 방법이 있다.
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# 타겟넘버를 만드는 방법의 수를 찾아라.

answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if (idx == N and target == value):
        answer += 1
        return
    if (idx == N):
        return
    DFS(idx+1, numbers, target, value+numbers[idx])
    DFS(idx+1, numbers, target, value-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer