class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        convert_type = str(x)
        n = len(convert_type)
        middle = n//2

        for i in range(middle):
            if convert_type[i] != convert_type[-1-i]:
                return False
            else:
                return True

sol = Solution()
print(sol.isPalindrome(121))
