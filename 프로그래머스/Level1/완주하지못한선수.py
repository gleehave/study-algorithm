# 1명을 제외하고, 모든 선수가 마라톤을 완주하였다.

# participant에는 참여 선수의 이름들이 있다.
# completion에는 완주한 이름이 들어있다.
# 동명이인이 있을 수 있다.

# 이때, 완주하지 못한 선수의 이름을 return

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for runner in participant:
        hashDict[hash(runner)] = runner
        sumHash += hash(runner)

    for complet in completion:
        sumHash -= hash(complet)

    return hashDict[sumHash]

print(solution(participant, completion))