# 학생들의 번호는 체격순으로 되어있음.
# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 빌려줄 수 있다.

# 4번 학생은 3번, 5번 학생에게만 빌려줄 수 있음.
# 체육복을 적절히 빌려, 최대한 많은 학생이 체육수업을 들어야함.

# n = 전체학생
# lost = 체육복이 없는 학생들의 번호
# reserve = 여벌의 체육복이 있는 학생들의 번호

# 여벌이 있는 학생이 도난 목록에 있을 경우, 자기 자신이 입어야 한다.

n  = 5
lost = [1,2,3,4,5]
reserve = []
# reserve = [1, 3, 5]
# return 5
def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for reserve_person in reserve_set:
        if reserve_person - 1 in lost_set:
            lost_set.remove(reserve_person - 1)
        elif reserve_person + 1 in lost_set:
            lost_set.remove(reserve_person + 1)

    return n - len(lost_set)


# def solution(n, lost, reserve):
#     check = [False] * (n+1) # 인덱스 1번 부터다!
#
#     for i in range(1, n+1):
#         if i not in lost:
#             check[i] = True
#
#     for no in lost: # no = 2
#         if no in reserve:
#             check[no] = True
#             reserve.remove(no)
#         elif (no-1) in reserve:
#             check[no] = True
#             reserve.remove(no-1)
#         elif (no + 1) in reserve:
#             check[no] = True
#             reserve.remove(no+1)
#
#     return sum(check)

print(solution(n, lost, reserve))