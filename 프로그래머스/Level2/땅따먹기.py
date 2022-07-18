# N행 4열로 이루어져 있다.
# 모든 칸에는 점수가 있다.
# 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 한다.
# 단, 연속한 같은 열을 밟을 수 없다.

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)

    return max(land[-1])