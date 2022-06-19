# 0~9 까지 카드를 4세트를 섞은 후,
# 6개의 카드를 골랐을 때,
# 연속인 숫자가 3개 이상이면 run
# 같은 숫자가 3개 이상이면 triplet이라 한다.

# 먼저 run 혹은 triplet이 되는 사람이 승자가 된다.
# 무승부인 경우, 0을 출력한다.

T = int(input())
for test_case in range(1,T+1):
    N = list(map(int,input().split()))
    A = [0,0,0,0,0,0,0,0,0,0]
    B = A.copy()
    result = 0
    for n in range(0,len(N),2):
        A[N[n]] += 1
        B[N[n+1]] += 1
        for i in range(1,9):
            if max(A) >= 3 or (A[i-1] >= 1 and A[i] >= 1 and A[i+1] >= 1) :
                result = 1
                break
        if result > 0:
            break
        for i in range(1,9):
            if max(B) >= 3 or (B[i-1] >= 1 and B[i] >= 1 and B[i+1] >= 1) :
                result = 2
                break
        if result > 0 :
            break
    print("#%d %d" % (test_case,result))
