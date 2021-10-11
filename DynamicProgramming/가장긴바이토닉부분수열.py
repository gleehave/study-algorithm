n=int(input())
a = list(map(int,input().split()))
dl=[1]*1000
dr=[1]*1000
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dl[i] = max(dl[i],dl[j]+1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j]:
            dr[i] = max(dr[i], dr[j]+1)
MAX = 0
for i in range(n):
    if dl[i] + dr[i] > MAX:
        MAX = dl[i] + dr[i]
print(MAX-1)



'''
N = int(input())
A = list(map(int, input().split()))
max_value = max(A)

for index in range(N):
    if A[index] == max_value:
        max_index = index
print('max index: ' , max_index)


count = 1
if max_index != 0:
    for i in range(max_index, 0, -1):
        print('i:', i)
        if A[i] > A[i-1]:
            count += 1
            print('[i]count: ',count)

    for j in range(max_index, N):
        print('j:', j)
        if j == N:
            if A[j-1] > A[j]:
                count += 1
                break
        if A[j] > A[j+1]:
            count += 1
            print('[j]count: ',count)

if max_index == 0:
    for i in range(N):
        if i == N-1:
            break
        if A[i] > A[i+1]:
            count += 1
print('result: ', count)
'''

