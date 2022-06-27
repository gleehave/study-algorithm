# n개의 음이 아닌 정수들이 있다.
# 이 정수들의 순서를 바꾸지 않고, 적절히 더하거나 빼서 타겟넘버를 만든다.

# [1,1,1,1,1]로 3을 만들려면, 5가지 방법이 있다.
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# 타겟넘버를 만드는 방법의 수를 찾아라.

def dfs(numbers, target, depth):
    count = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        count += dfs(numbers, target, depth+1)
        numbers[depth] *= -1
        count += dfs(numbers, target, depth-1)
        return count

def solution(numbers, target):
    count = dfs(numbers, target, 0)
    return count