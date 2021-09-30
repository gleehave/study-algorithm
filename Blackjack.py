#카지노에서 제일 인기있는 게임 블랙잭의 규칙은 
#카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다.
# 각 카드는 양의 정수를 갖는다.
# N장의 카드를 모두 숫자가 보이도록 한다.
# 숫자 M을 부르면, N장의 카드에서 3장을 골라 M을 넘지 않으면서, M과 최대한 가깝게 만들어야 한다.

# N장의 카드가 주어졌을때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구하라.

Count, M = map(int, input().split(' '))
N = list(map(int,input().split(' ')))

res=0
for i in range(0,Count-2):
    for j in range(i+1, Count-1):
        for k in range(j+1, Count):
            if N[i] + N[j] + N[k] > M:
                continue
            else:
                res = max(res, N[i] + N[j] + N[k])

print(res)