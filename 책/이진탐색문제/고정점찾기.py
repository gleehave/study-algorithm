# 고정점(Fixed Point): 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
# a = {-15, -4, 2, 8, 13} 일 때, a[2]=2이므로 고정점은 2가 된다.

# 하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있다.
# 이때, 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램
# 만약 고정점이 없다면 -1을 출력한다.

def binary_search(array, start, end):
    if start > end:
        return None

    mid = (start+end)//2

    if array[mid] == mid:
        return mid

    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)

n = int(input())
array = list(map(int, input().split()))
index = binary_search(array, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)

'''
N = int(input())
data = list(map(int, input().split()))

init_start = 0
init_end = len(data)-1
mid = init_end//2


while True:
    print('while')
    if mid == data[mid]:
        print(mid, end=' ')
        break
    if mid == init_start or mid == init_end:
        print(-1)
        break

    if mid > data[mid]:
        start = mid+1
        mid = (start+mid)//2

    if mid < data[mid]:
        end = mid-1
        mid = (start+mid)//2
'''