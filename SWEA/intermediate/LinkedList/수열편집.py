T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())  # 수열의 길이, 추가 횟수, 출력할 인덱스 번호
    numbers = list(map(int, input().split()))  # 수열
    for _ in range(M):
        edit = list(input().split())
        if edit[0] == 'I':  # 삽입
            numbers.insert(int(edit[1]), int(edit[2]))
        elif edit[0] == 'C':  # 바꾸기
            numbers[int(edit[1])] = int(edit[2])
        elif edit[0] == 'D':  # 삭제
            numbers.pop(int(edit[1]))

    try:
        result = numbers[L]
    except:
        result = -1
    print(f"#{test_case} {result}")