class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        for i in range(2,n-1):
            temp = n
            change_base = ''
            while temp>0:
                change_base = str(temp%i)+change_base
                temp = temp//i
            if change_base != change_base[::-1]:
                return False
        return True