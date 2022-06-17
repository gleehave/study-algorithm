# A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려준다.
# 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이긴다.
# L : 1 / R: 400 / C : int(L+R)/2)
# 찾는 쪽 번호가 C와 같아지면 탐색이 끝난다.

# P: 전체 쪽 수

def binary_search(P, target):
    L = 1
    R = P
    count = 1

    while L <= R:
        mid = int((L+R)/2)
        if mid == target:
            return count
        elif mid < target:
            L = mid
            count += 1
        elif mid > target:
            R = mid
            count += 1


T = int(input())
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())

    Pa = binary_search(P, A)
    Pb = binary_search(P, B)

    if Pa > Pb:
        print("#{} B".format(test_case))
    elif Pa < Pb:
        print("#{} A".format(test_case))
    else:
        print("#{} 0".format(test_case))

