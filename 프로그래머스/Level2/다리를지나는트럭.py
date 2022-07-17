# 모든 트럭이 다리를 건너려면 최소 몇초가 필요한가?

# bridge_length 는 다리에 최대로 올라갈 수 있는 트럭대수
# weight는 버틸 수 있는 하중

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
# result 8초

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]

    while bridge:
        answer += 1
        bridge.pop(0)

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
    return answer