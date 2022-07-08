# 스코빌 지수가 가장 낮은 2개의 음식을 골라서 새로운 음식을 만든다.

# 섞은 음식의 스코빌 지수 =
#     가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복한다.

# 이때, 모든 음식이 K이상의 스코빌 지수가 되기까지 최소 섞는 횟수는?

scoville = [1,2,3,9,10,12]
K = 7
# 1 + (2*2) = 5 -> [5, 3, 9, 10, 12]
# 3 + (5*2) = 13 -> [13, 9, 10, 12]

import heapq

def solution(scoville, K):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    count = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap)*2))
        except IndexError:
            return -1
        count += 1

    return count

print(solution(scoville,K))