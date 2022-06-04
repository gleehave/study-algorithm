# 가로 W, 세로 H

# 최대 공약수 구한다. ex) 8, 12 -> 최대 공약수 4
# (0,0) -> (2,3) -> (4,6) -> (6,9) -> (8,12)


def func(w, h):
    a, b = max([w, h]), min([w, h])
    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r

def solution(w,h):
    squares = w * h
    gcd = func(w, h)

    return squares - (w + h - gcd)