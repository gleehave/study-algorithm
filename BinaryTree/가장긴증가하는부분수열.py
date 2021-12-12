
N = int(input())
A = list(map(int, input().split()))

memory = [0]

for case in A:
    if memory[-1] < case:
        memory.append(case)
    else:
        left = 0
        right = len(memory)
        while left < right:
            mid = (left + right) // 2
            if memory[mid] < case:
                left = mid + 1
            else:
                right = mid
        memory[right] = case

print(len(memory)-1)