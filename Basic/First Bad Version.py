# You are a product manager and currently leading a team to develop a new product.
# the latest version of your product fails the quality check.
# since each version is developed based on the previous version,
# all the versions after a bad version are also bad.

# suppose you have n versions [1,2,3,... ,n]
# and you want to find out the first bad one, which causes all the following ones to be bad.
# Implement a function to find the first bad version
# you should minimize the number of calls to the API.

# input : n=5, bad=4
# output: 4

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version, bad):
    if version >= bad:
        print("call isBadVersion(", version, ") -> True")
        return True
    # isBadVersion이 True면, 불량이다.
    else:
        print("call isBadVersion(", version, ") -> False")
        return False
    # isBadVersion이 False면, 정상이다.

# n = [1,2,3,4,... n]
# bad = 4   # 4,5는 불량이다.

def firstBadVersion(n, bad):
    # index도 배열과 똑같이 진행한다.
    left = 1
    right = n

    while left < right:
        mid = (right + left) // 2
        if isBadVersion(mid, bad):
            right = mid
        else:
            left = mid + 1
    return left

print(firstBadVersion(1,1))