# 00시 00분 00초 부터 N시 59분 59초 까지, '3' 숫자가 입력받은 숫자만큼 포함되는 경우의 수를 구하라.

h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)