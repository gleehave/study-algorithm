N, M = map(int, input().split())
line = []
mini = []

for _ in range(N):
    line.append(input())
print('line: ', line)

for a in range(N-7):
    print('a: ', a)
    for i in range(M-7):
        print('i: ',i)
        idx1 = 0
        idx2 = 0
        for b in range(a,a+8):
            print('b: ',b)
            for j in range(i,i+8):
                print('j: ',j)
                if (j+b)%2 == 0:
                    if line[b][j] != 'W': idx1 += 1
                    if line[b][j] != 'B': idx2 += 1
                else:
                    if line[b][j] != 'B': idx1 += 1
                    if line[b][j] != 'W': idx2 += 1
        mini.append(idx1)
        mini.append(idx2)

print(min(mini))