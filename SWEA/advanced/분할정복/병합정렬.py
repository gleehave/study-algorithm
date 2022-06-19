# 오름차순으로 정렬
# N개의 정렬 대상을 가진 리스트 L을 분할할 때,
# L[0:N//2],  L[N//2:N] 으로 분할한다.

# 병합과정에서
# 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.

# 정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.

def partition(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left_lst = partition(lst[:mid])
    right_lst = partition(lst[mid:])
    return merge(left_lst, right_lst)

def merge(left_lst, right_lst):
    global count
    left_N = len(left_lst)
    right_N = len(right_lst)
    result = [0]*(left_N + right_N)
    left_i, right_i = 0, 0
    i = 0

    if left_lst[-1] > right_lst[-1]:
        count += 1

    while left_i < left_N or right_i < right_N:
        if left_i < left_N and right_i < right_N:
            if left_lst[left_i] <= right_lst[right_i]:
                result[i] = left_lst[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right_lst[right_i]
                i += 1
                right_i += 1
        elif left_i < left_N:
            result[i] = left_lst[left_i]
            i += 1
            left_i += 1
        elif right_i < right_N:
            result[i] = right_lst[right_i]
            i += 1
            left_i += 1
        elif right_i < right_N:
            result[i] = right_lst[right_i]
            i+= 1
            right_i += 1
    return result

T = int(input())
for test_case in range(1, T+1):
    count = 0
    N = int(input())
    lst = list(map(int, input().split()))
    data = partition(lst)

    print("#{} {}".format(test_case, count))