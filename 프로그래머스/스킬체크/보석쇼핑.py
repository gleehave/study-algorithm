
# 모든 보석을 1개 이상 포함하는 가장 짧은 구간을 찾고싶다.
# "시작 진열 번호" 와 "끝 진열 번호" 를 return 하라.

                         # 3번                               # 7번
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# result = [3, 7]

def solution(gems):
    answer = []
    shortest = len(gems) + 1

    start_p = 0
    end_p = 0

    check_len = len(set(gems)) # 종류별 보석
    contained = {}

    while end_p < len(gems):
        if gems[end_p] not in contained:
            contained[gems[end_p]] = 1
        else:
            contained[gems[end_p]] += 1
        end_p += 1

        print("start_p", start_p)
        print("end_p:", end_p)
        print("len(contained): ", len(contained))

        if len(contained) == check_len:
            print("contained:", contained)
            while start_p < end_p:
                if contained[gems[start_p]] > 1:
                    contained[gems[start_p]] -= 1
                    start_p += 1
                elif shortest > end_p - start_p:
                    shortest = end_p - start_p
                    print("shortest:", shortest)
                    answer = [start_p+1, end_p]
                    break
                else:
                    break
    return answer

print(solution(gems))