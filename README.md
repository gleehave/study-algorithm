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
  - Counter('hello world').most_common() 을 하면 데이터 개수가 많은 수느올 정렬된 배열을 리턴한다.
    - [('l',3), ('o',2), ('h',1) ...]
    - Counter('hello world').most_common(1) # [('l',3)]
- heqpq: 힙(heap) 자료구조 제공
  - 일반적으로 우선순위 큐 기능을 사용
- bisect: 이진탐색(binary search) 기능 제공
- collections: 덱(deque), 카운터(counter) 등의 유용한 자료구조 포함

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

## Problem
/Basic <br>
- [기초] 기초적인 파이썬 문법 연습장

/Bruteforce <br>
- [블랙잭]https://www.acmicpc.net/problem/2798 <br>
- [분해합]https://www.acmicpc.net/problem/2231 <br>
- [덩치] https://www.acmicpc.net/problem/7568 <br>
- [체스판칠하기] https://www.acmicpc.net/problem/1018 <br>
- [큰 수의 법칙] chapter 03, 93p. <br>
- [숫자 카드 게임] chapter 03, 96p. <br>
- [1이 될 때까지] chapter 03, 99p. <br>

/Stack <br>
- [스택] https://www.acmicpc.net/step/11 <br>
- [괄호]https://www.acmicpc.net/problem/9012 <br>

/DynamicProgramming <br>
- <참고자료> https://galid1.tistory.com/507 <br>
- [가장긴바이토닉부분수열] https://www.acmicpc.net/problem/11054 <br>
- [정수삼각형] https://www.acmicpc.net/problem/1932 <br>

/Queue <br>
- [요세푸스문제] https://www.acmicpc.net/problem/11866 <br>
- [덱] https://www.acmicpc.net/problem/10866 <br>

/Divide&Conquer <br>
- [종이의개수] https://www.acmicpc.net/problem/1780 <br>
- [색종이만들기] https://www.acmicpc.net/problem/2630 <br>

/BinaryTree <br>
- [가장긴증가하는부분수열2] https://www.acmicpc.net/problem/12015 <br>
- [트리순회] https://www.acmicpc.net/problem/1991

/PriorityQueue <br>
- [절대값힙] https://www.acmicpc.net/problem/11286 <br>

/프로그래머스 <br>
- Level1
  - [Level1] https://programmers.co.kr/learn/courses/30/lessons/77484<br>
  - [Level1] https://programmers.co.kr/learn/courses/30/lessons/72410<br>
  - [Level1] https://programmers.co.kr/learn/courses/30/lessons/81301<br>
  - [Level1] https://programmers.co.kr/learn/courses/30/lessons/67256<br>
  - [Level1] https://programmers.co.kr/learn/courses/30/lessons/86051<br>
  - [Level1] https://programmers.co.kr/learn/courses/30/lessons/17681<br>
  - [Level1] https://programmers.co.kr/learn/courses/30/lessons/68644<br>
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