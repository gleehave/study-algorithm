# 500원, 100원, 50원, 10원 짜리 동전이 무한히 존재한다.
# 손님에게 거슬러 줘야 할 돈이 n 원일때, 거슬러 줘야 할 동전의 최소 개수는?

n = 1260
count = 0

coins = [500,100,50,10]

for coin in coins:
    count = count + (n // coin)
    n = n % coin

print(count)
