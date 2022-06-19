# N개의 정수를 정렬해
# 리스트 A에 넣고, A[N//2]에 저장된 값을 출력한다.

def quicksort(left, right):
    if left >= right:
        return

    pivot = left
    i = left+1
    j = right-1
    while i <= j:
        while i <= j and a[pivot] >= a[i]:
            i += 1
        while i <= j and a[pivot] <= a[j]:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]

    a[pivot], a[j] = a[j], a[pivot]

    quicksort(left, j)
    quicksort(j+1, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    quicksort(0, len(a))
    print("#{} {}".format(tc, a[N//2]))