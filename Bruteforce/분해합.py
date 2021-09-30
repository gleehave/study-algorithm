N = int(input())

for i in range(1,N+1):
    value = sum(map(int, str(i)))
    res_value = i + value
    
    if res_value == N:
        print(i)
        break
    if i == N:
        print(0)