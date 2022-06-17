class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def addList(lst, new):
    if lst.head is None:
        lst.head = new
        new.prev = new.next = new
    else:
        tail = lst.head.prev
        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new
    lst.size += 1


def printList(lst):  # 연결리스트 출력
    if lst.head is None:
        return

    cur = lst.head.prev
    cnt = lst.size
    if lst.size > 10:  # 최대 10개이하로 출력
        cnt = 10
    for _ in range(cnt):
        print(cur.data, end=' ')
        cur = cur.prev
    print()


# import sys
# sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))  # 1차원 배열
    mylist = LinkedList()
    for val in arr:
        addList(mylist, Node(val))

    cur = mylist.head
    for _ in range(K):  # 반복 K
        for _ in range(M):  # 추가 M
            cur = cur.next
        prev = cur.prev
        new = Node(prev.data + cur.data, prev, cur)
        prev.next = new
        cur.prev = new
        cur = new  # 새로 추가된 위치를 시작위치로 재설정
        mylist.size += 1
    print(f'#{tc}', end=' ')
    printList(mylist)