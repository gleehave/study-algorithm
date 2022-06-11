def solution(prices):
    answer = [0]*len(prices)
    stack = []

    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j

        # stack에 index를 저장한다.
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = len(prices)-1-j
    return answer

prices = [1, 2, 3, 2, 3]
solution(prices)