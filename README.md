# Study Algorithm

첫째, 알고리즘 연습과 자료구조를 이해하고자 함. <br>
둘째, 코드를 작성하는 것의 두려움을 없애보자. <br>

## Getting Started

백준의 알고리즘 유형을 풀어본다. <br>
"단계별로 풀어보기" 에 해당하는 문제를 우선으로 한다. <br>
https://www.acmicpc.net/step  <br>

프로그래머스 Level1 ~ Level2 <br>
https://programmers.co.kr/ <br>

## Standard library!
- 내장함수: 기본 입출력 함수부터 정렬 함수까지 기본적인 함수
- itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 기능 제공
  - 특히 순열, 조합 라이브러리 자주 사용!
  - from itertools import permutations, product
  - from itertools import combinations, combinations_with_replacement
      - combinations라는 내장함수(built-in)을 이용하여 인자값에 따라 해당 요소로 구할 수 있는 모든 조합을 리턴한다.
      - combinations(numbers, 2) -> numbers 리스트 안에 2개의 요소로 구할 수 있는 모든 조합을 반환
      - for li in combinations(menu_li, k): # combinations 함수를 통해 만들고, 1개씩 접근
- Counter: collections 모듈의 Counter 클래스 제공함. 데이터의 개수를 셀 때, 주로 이용한다.
  - Counter('hello world') # Counter({'l':3, 'o':2, 'h':1, 'e':1 .....})
  - Counter('hello world').most_common() 을 하면 데이터 개수가 많은 수를 정렬된 배열을 리턴한다.
    - [('l',3), ('o',2), ('h',1) ...]
    - Counter('hello world').most_common(1) # [('l',3)]
- heqpq: 힙(heap) 자료구조 제공
  - 일반적으로 우선순위 큐 기능을 사용
- bisect: 이진탐색(binary search) 기능 제공
- collections: 덱(deque), 카운터(counter) 등의 유용한 자료구조 포함
  - from collections import deque 혹은 import Queue 를 선언하여 queue 자료구조를 활용할 수 있다.

## 내가 항상 놓치는 부분!
- Python에서 리스트, 문자열의 원소가 있는지 체크 하고 싶으면, if value in array: 를 하면 True일 때를 체크할 쉽게 체크할 수 있다.
- array안에서 특정 원소의 개수를 알고 싶으면, array.count(3), array.count('apple')를 사용해서 쉽게 개수를 알 수 있다.
- 문자열에서 일부 값을 변경하고 싶다면, array.replace('..', '.') 를 하면 쉽게 변경할 수 있다.
- value.isdigit(), value.isalpha() 을 통해서 문자열의 type을 확인할 수 있다.
- 거리 계산이나 경로를 찾을 때, 좌표계형태로 반드시 생각해볼 것!
- 좌표계일 때, 거리는 행과 열을 모두 계산할 것!
- 10진수를 binary 2진수로 나타낼 때, bin(9)[2:] 를 하면 자동으로 변환해줌. bin(i): 0b1001 
- arr이 배열일 때, arr.rjust(n, '0')를 하면 n의 자릿수만큼 '0'을 채워줌. '0'외에 다른 값도 가능
    - arr=[1,0,0,1], n=5 이면 arr.rjust : [0,1,0,0,1]
    - arr=[1,0,0,1], n=5 이면 arr.ljust : [1,0,0,1,0]
- '구분자'.join(리스트) : join함수는 매개변수로 들어오는 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환한다.
  - ''.join(['a','b','c']) # 'abc'로 반환
- BFS 경로를 찾을 때, queue를 사용한다. 또한, 주어진 값과 비교할 수 있는 지나간 경로를 기억할 수 있는 좌표가 필요하다!
- '문자열'.startswith(str or tuple) 형식으로 하면, 대소문자를 구분해서 문자열이 string에 있으면 true, 없으면 false를 반환
- 괄호변환 같은 키워드의 문제는 stack으로 접근해서, append, pop을 이용해서 괄호의 짝이 맞는지 검사할 수 있도록 접근한다.
  - 괄호변환 뿐만 아니라, 짝을 맞추는 검사를 해야한다면 stack 자료구조를 이용해보자
- DP관련 문제 (e.g., 타일링문제)에 대해서는 규칙성을 점화식으로 나타낸 후 code를 작성한다.
  - D(n) = D(n-1)+D(n-2) 의 형태로 나타낸 후, 재귀적으로 풀어낼 수 있다.
  - [DP] https://www.youtube.com/watch?v=YHZiWaL49HY
- str.isdigit() : 문자열이 '숫자'로 이루어졌는지 확인하는 함수.
- 백트래킹: 해를 찾는 도중 해가 아니면 되돌아가서 다시 해를 찾는다.
  - DFS는 모든 경우를 전부 찾는다.
  - 해가 없는 경로를 조건으로 걸어두면, 경로를 더이상 가지 않고, 되돌아간다.
  - DFS과 같이 모든 경우의 수를 탐색하는 과정에서, 조건문 등을 걸어 답이 절대로 될 수 없는 상황을 정의하고, 
  - 그러한 상황일 경우에 탐색을 중지시킨 뒤 이전으로 돌아가서 다시 다른 경우를 탐색하는 것으로 구현한다.
  - [backtracking] https://chanhuiseok.github.io/posts/algo-23/
  - [backtracking] https://www.youtube.com/watch?v=Ar40zcPoKEI
- 힙(heap): 완전 이진트리에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위한 자료구조
  - 힙은 최대힙(max heap)과 최소힙(min heap)이 있다.
  - import heapq (파이썬에서 heapq 모듈은 기본적으로 최소힙이다.)
    ```
    max_heap = []
    for item in heap_items:
        heapq.heappush(max_heap, (-item, item))
    
    heap = [50, 10, 20] # 미리 생성해둔 리스트가 있을 때,
    heap.heapify(heap)
    print(heap) # [10, 50, 20] 이 출력된다. 
    
    # 최소 힙
    import heapq
    def heapsort(iterable):
      h = []
      result = []
      for value in iterable:
        heapq.heappush(h, value)
      for i in range(len(h)):
        result.append(heapq.heappop(h))
      return result
    
    # [1,3,5,7,9,2,4,6,8,0] 
    # result: [0,1,2,3,4,5,6,7,8,9]
    
    # 최대힙
    import heapq
    def heapsort(iterable):
      h = []
      result = []
      for value in iterable:
        heapq.heappush(h, -value) # 여기에 음수를 붙인다.
      for i in range(len(h)):
        result.append(-heapq.heappop(h)) # 꺼낼때, 다시 음수를 붙인다.
      return result
    
    # [1,3,5,7,9,2,4,6,8,0] 
    # result: [9,8,7,6,5,4,3,2,1,0]
    ```
    heapq.heappush(heap, item) / heapq.heapqpop(heap) / heapq.heapify(list) : 리스트를 heap으로 변환
- 문자열 바이너리 변환
  - string = "Python"
  - binary = ' '.join(format(ord(c), 'b') for c in string)
  - binary = ' '.join(format(ord(c), 'b') for c in bytearray(string, 'utf-8'))
  - binray = ' '.join(map(bin, bytearray(string, 'utf-8')))
- 다익스트라 최단경로 알고리즘
  ```
  1. 출발 노드를 설정한다.
  2. 최단 거리 테이블을 초기화한다.
  3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
  4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하고, 최단 거리 테이블을 갱신한다.
  5. 3번과 4번 과정을 반복한다.
  ```
- 인접행렬(Adjacency Matrix), 인접리스트(Adjacency List)
  ```
  # 인접행렬
  graph = [
      [0, 7, 5],
      [7, 0, INF],
      [5, INF, 0]
  ]
  
  # 인접리스트
  graph = [[] for _ in range(3)]
  graph[0].append((1, 7))
  graph[0].append((2, 5))
  graph[0].append((0, 7))
  graph[0].append((0, 5))
  # [[(1,7), (2,5)], [(0, 7)], [(0, 5)]]
  ```

## Stack
```
stack = []
ans = 1
string = str(input())

arr = list(string)
for i in range(0, len(arr)):
  if arr[i] == '(' or arr[i] == '{':
    stack.append(arr[i])
  elif arr[i] == ')' or arr[i] == '}':
    if not stack:
      ans = 0
      break
    
    P = stack.pop()

    if arr[i] == ')' and P != '(':
      ans = 0
    elif arr[i] == '}' and P != '{':
      ans = 0

if stack:
  ans = 0
```

## Graph
```
T = int(input())
for tc in range(1, T+1):
  V, E = map(int, input().split())
  node = [[] for _ in range(V+1)]
  for _ in range(E):
    start, end = map(int, input().split())
    node[start].append(end)
  
  S, G = map(int, input().split())
  stack = [S]
  visited = [False for ) in range(V+1)]
  
  while stack:
    now = stack.pop()
    visited[now] = True
    for next in node[now]:
      if not visited[next]:
        stack.append(next)
  
  if visited[G]:
    result = 1
  else:
  result = 0
```
 
## DFS
```
def dfs(y, x):
  global res
  data[y][x] = 1
  for d in range(4):
    xf = dx[d] + x
    yf = dy[d] + y
    if (0 <= xf < N) and (0 <= yf < N):
      if data[yf][xf] == 0:
        dfs(yf, xf)
      if data[yf][xf] == 3:
        res = 1
        return
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = 0
dfs(y, x)
```

## BFS
```
def bfs(start_y, start_x):
  global D_result
  Q.append((start_y, start_x))
  visited.append((start_y, start_x))
  
  while Q:
    start_y, start_x = Q.pop(0)
    for dir in range(4):
      newY = start_y + dy[dir]
      newX = start_x + dx[dir]
      if IsSafe(newY, newX) and (newY, newX) not in visited:
        Q.append((newY, newX))
        Distance[newY][newX] = Distance[start_y][start_x]+1
        if Maze[newY][newX] == 3:
          D_result = Distance[newY][newX] - 1
          return
-----------------------------------------------------------------
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for node in range(n):
        if visited[node] == False:
            bfs(n, computers, node, visited)
            answer += 1
    return answer

def bfs(n, computers, node, visited):
    visited[node] = True
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        visited[node] = True
        for connect in range(n):
            if connect != node and computers[node][connect] == 1:
                if visited[connect] == False:
                    q.append(connect)
```

## DP
```
def function(N):
  if N % 10 == 0:
    if N == 10:
      return 1
    elif N == 20:
      return 3
    else:
    return function(N-10) + (2 * function(N-20))
```

## Backtracking
```
def backtracking(i, N, S, visited):
  global sumV
  if i == N:
    if s < sumV:
      sumV = s
  elif s > sumV:
    return
  else:
    for j in range(N):
      if not visited[j]:
        visited[j] = 1
        backtracking(i+1, N, s+num_list[i][j], visited)
        visited[j] = 0

T = int(input())
for test_case in range(T):
  N = int(input())
  num_list = [list(map(int, input().split())) for _ in range(N)]
  sumV = 100
  visited[0] * N
  backtracking(0, N, 0, visited)
```

## Divide & Conquer
```
def rsp(a, b):
  if data[a] == data[b]:
    return a
  elif (data[a] - data[b] == 1) or (data[a]-data[b] == -2):
    return a
  return b

def divide(start, end):
  if start == end:
    return start
  a = divide(start, (start+end)//2)
  b = divide((start+end)//2+1, end)
  return rsp(a, b)

result = divide(0, N-1)
----------------------------------------
def merge_sort(m):
  if len(m) <= 1:
    return m
  mid = len(m)//2
  left = m[:mid]
  right = m[mid:]
  
  left = merge_sort(left)
  right = merge_sort(right)
  
  return merge(left, right)

def merge(left, right):
  result = []
  
  while len(left) > 0 and len(right) > 0:
    if left[0] <= right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))
  
  if len(left) > 0:
    result.extend(left)
  
  if len(right) > 0:
    result.extend(right)
  
  return result
```

## Binary Search
```
def binary_search(a, key):
  start = 0
  end = len(a) -1 
  while start <= end:
    middle = start + (end-start) // 2
    if key == a[middle]:
      return middle
    elif key < a[middle]:
      end = middle - 1
    else:
      start = middle + 1
  return -1

def binary_search(a, low, high, key):
  if low > high:
    return -1
  else:
    middle = (low+high) // 2
    if key == a[middle]:
      return middle
    elif key < a[middle]:
      return binary_search(a, low, middle-1, key)
    else:
      return binary_search(a, middle+1, high, key)
```

## Prim
```
# pi = 간선정보
# key = pi에 저장된 가중치

def MST(G, S):
  key = [INF] * N
  pi = [None] * N
  visited = [False] * N
  key[S] = 0
  
  for _ in range(N):
    minIndex = -1
    min = INF
    for i in range(N):
      if not visited[i] and key[i] < min:
        min = key[i]
        minIndex = i
    
    visited[minIndex] = True
    
    for v, val in G[minIndex]:
      if not visited[v] and val < key[v]:
        key[v] = val
        pi[v] = minIndex
```

## Kruskal
```
class disjoinset:
  def __init__(self):
    self.parent = None

def unionset(set1, set2):
  set2 = findset(set2)
  set2.parent = set1
  
def findset(set):
  while set.parent != None:
    set = set.parent
  return set

def kruskal(graphs, weights):
  mst_graphs = [[0 for _ in range(len(graphs))] for _ in range(len(graphs))]
  vertex_sets = [disjoinset() for _ in range(len(graphs))]
  visited = set()
  heap = []
  
  for vertex in range(len(graphs)):
    for target in range(vertex, len(graphs)):
      if weights[vertex][target] > 0:
        heapq.heappush(heap, (weights[vertex][target], vertex, target))
  
  weight_sum = 0
  while len(heap) > 0:
    pop = heapq.heappop(heap)
    w = pop[0]
    v1 = pop[1]
    v2 = pop[2]
    set1 = vertex_sets[v1]
    set2 = vertex_sets[v2]
    
    if findset(set1) != findset(set2):
      unionset(set1, set2)
      mst_graphs[v1][v2] = 1
      mst_graphs[v2][v1] = 1
      weight_sum += weights[v1][v2]
-----------------------------------------------
from heapq import heappop, heappush

def find(x):
  if parents[x] == x:
    return x
  parents[x] = find(parents[x])
  return parents[x]

def union(a, b):
  a = find(a)
  b = find(b)
  if a > b:
    a, b = b, a
  parents[b] = a

for test in range(1, int(input())+1):
  V, E = map(int, input().split())
  parents = {i: i for i in range(V+1)}
  edges = []
  
  for _ in range(E):
    a, b, w = map(int, input().split())
    heappush(edges, (w, a, b))
  
  answer = 0
  while edges:
    w, a, b = heappop(edges)
    if find(a) != find(b)
      union(a, b)
      answer += w
  
  print("#{} {}".format(test, answer)
```

## Dijkstra
```
def Dijkstra(G, r):
  D = [INF]*N
  P = [None]*N
  visited = [False]*N
  D[r] = 0
  
  for _ in range(N):
    minIndex = -1
    min = INF
    for i in range(N):
      if not visited[i] and D[i] < min:
        min = D[i]
        minIndes = i
    visited[minIndex] = True
    for v, val in G[minIndex]:
      if not visited[v] and D[minIndex] + val < D[v]:
        D[v] = D[minIndex] + val
        P[v] = minIndex
```

## 버블정렬
```
array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
```

## 선택정렬
```
array = [8,4,6,2,9,1,3,7,5]

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
```

## 삽입정렬
```
array = [8,4,6,2,9,1,3,7,5]

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
```

## 병합정렬
```
array = [8,4,6,2,9,1,3,7,5]

def merge_sort(array):
    if len(array) < 2: # array가 1개이다.
        return array
    
    mid = len(array) // 2
    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])
    
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    
    return merged_arr
```

## 퀵정렬
```
array = [8,4,6,2,9,1,3,7,5]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = len(array)//2
    front_arr, pivot_arr, back_arr = [], [], []
    for value in array:
        if value < array[pivot]:
            front_arr.append(value)
        elif value > array[pivot]:
            back_arr.append(value)
        else:
            pivot_arr.append(value)
    return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr) 
```

## 단일 연결 리스트
```
class SLinkedList:
    def __init__(self):
        self.head = None
    
    class Node:
       def __init__(self, v, n=None):
           self.value = v
           self.next = n
        
    def insertNode(self, v): 
        if self.head is None :
            self.head = self.Node(v)
        else:
            self.head = self.Node(v,self.head)  
    
    def printNode(self):
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            print("<현재 리스트 구조>", end='\t') #end로 print 마지막 개행을 변경할 수 있습니다.
            link = self.head #처음은 head를 지정. 이후부터는 현 노드의 next를 지정
    
            while link :
                print(link.value, '->' , end = ' ')
                link = link.next #link를 현 위치 노드의 next로 변경
    
    def deleteNode(self):
        if self.head is None :
            print("삭제할 노드가 없습니다.")
            return
        else:
            #head를 현 head의 next. 즉, 다음 노드로 변경.
            self.head = self.head.next            
```

## Basic <br>
  - [기초] 기초적인 파이썬 문법 연습장

## Bruteforce
  - [블랙잭]https://www.acmicpc.net/problem/2798 <br>
  - [분해합]https://www.acmicpc.net/problem/2231 <br>
  - [덩치] https://www.acmicpc.net/problem/7568 <br>
  - [체스판칠하기] https://www.acmicpc.net/problem/1018 <br>
  - [큰 수의 법칙] chapter 03, 93p. <br>
  - [숫자 카드 게임] chapter 03, 96p. <br>
  - [1이 될 때까지] chapter 03, 99p. <br>
  
## Stack
  - [스택] https://www.acmicpc.net/step/11 <br>
  - [괄호]https://www.acmicpc.net/problem/9012 <br>

## DynamicProgramming <br>
  - <참고자료> https://galid1.tistory.com/507 <br>
  - [가장긴바이토닉부분수열] https://www.acmicpc.net/problem/11054 <br>
  - [정수삼각형] https://www.acmicpc.net/problem/1932 <br>

## Linked List
  - [문제로풀어보는 알고리즘] 34p.

## Queue
  - [요세푸스문제] https://www.acmicpc.net/problem/11866 <br>
  - [덱] https://www.acmicpc.net/problem/10866 <br>

## Divide&Conquer
  - [종이의개수] https://www.acmicpc.net/problem/1780 <br>
  - [색종이만들기] https://www.acmicpc.net/problem/2630 <br>

## BinaryTree
  - [가장긴증가하는부분수열2] https://www.acmicpc.net/problem/12015 <br>
  - [트리순회] https://www.acmicpc.net/problem/1991

## PriorityQueue
  - [절대값힙] https://www.acmicpc.net/problem/11286 <br>

## 프로그래머스
  - Level1
    - [Level1] https://programmers.co.kr/learn/courses/30/lessons/77484<br>
    - [Level1] https://programmers.co.kr/learn/courses/30/lessons/72410<br>
    - [Level1] https://programmers.co.kr/learn/courses/30/lessons/81301<br>
    - [Level1] https://programmers.co.kr/learn/courses/30/lessons/67256<br>
    - [Level1] https://programmers.co.kr/learn/courses/30/lessons/86051<br>
    - [Level1] https://programmers.co.kr/learn/courses/30/lessons/17681<br>
    - [Level1] https://programmers.co.kr/learn/courses/30/lessons/68644<br>
    - [Level1] https://programmers.co.kr/learn/courses/30/lessons/86491<br>
    - [Level1] https://programmers.co.kr/learn/courses/30/lessons/12903<br>
    - [Level1] https://programmers.co.kr/learn/courses/30/lessons/76501<br>
    - [Level1] https://school.programmers.co.kr/learn/courses/30/lessons/42840<br>
    - [Level1] https://school.programmers.co.kr/learn/courses/30/lessons/42862<br>
  - Level2
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/72411<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/62048<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/1844<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/49993<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/42885<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/70129<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/81302<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/42577<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/60058<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/42584<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/49994<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/43165<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/42586<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/42842<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/42888<br>
    - [Level2] https://programmers.co.kr/learn/courses/30/lessons/12909<br>
    - [Level2] https://school.programmers.co.kr/learn/courses/30/parts/12230<br>
    - [Level2] https://school.programmers.co.kr/learn/courses/30/lessons/42626<br>
  - Level3
    - [Level3] https://school.programmers.co.kr/learn/courses/30/lessons/43163<br>
    - [Level3] https://school.programmers.co.kr/learn/courses/30/lessons/43162<br>
    - [Level3] https://school.programmers.co.kr/learn/courses/30/lessons/43164<br>
    - [Level3] https://school.programmers.co.kr/learn/courses/30/lessons/49189<br>