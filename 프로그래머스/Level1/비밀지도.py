def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        arr12 = str(bin(i|j)[2:])
        arr12 = arr12.rjust(n, '0')
        arr12 = arr12.replace('1', '#')
        arr12 = arr12.replace('0', ' ')
        answer.append(arr12)

    return answer

n=5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(n,arr1,arr2)

'''
1. 한변의 길이가 n인 정사각형의 배열 (공백 혹은 #(벽) 으로 이루어져있음)
2. 전체 지도는 2장의 지도를 겹쳐서 얻을 수 있다.
    지도1과 지도2에서 하나라도 벽인 부분은 전체 지도에서 벽이다.
    지도1과 지도2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
3. 1은 벽을 의미한다. 0은 공백을 의미한다.
'''