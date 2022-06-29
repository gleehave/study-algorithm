# 항공권은 항상 "ICN" 에서 출발한다.
# 2차원 배열의 tickets가 주어진다.
# 방문하는 공항 경로를 배열에 담아 return

# 모든 공항은 대문자 3글자
# tickets의 [a, b]는 a에서 b공항으로 가는 것을 의미한다.
# 주어진 항공권은 모두 사용한다.
# 만일 가능한 경로가 2개 이상을 경우, 알파벳 순서가 앞에 오도록 return

# 1번 예제
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# return ["ICN", "JFK", "HND", "IAD"]

# 2번 예제
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# return ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

def solution(tickets):
    routes = dict()
    for ticket in tickets:
        if ticket[0] in routes:
            routes[ticket[0]].append(ticket[1])
        else:
            routes[ticket[0]] = [ticket[1]]
    # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}

    for key in routes.keys():
        routes[key].sort(reverse=True)
    # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']}

    answer = []
    start = ["ICN"]

    while start:
        target = start[-1]
        if target not in routes or len(routes[target]) == 0:
            answer.append(start.pop())
        else:
            start.append(routes[target].pop())
    return answer[::-1]

solution(tickets)