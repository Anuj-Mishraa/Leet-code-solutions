class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        i = 0
        temp = ""
        while i<=len(s):
            if i==len(s):
                res += temp[::-1]
            elif s[i]==" ":
                res += temp[::-1]+" "
                temp = ""
            else:
                temp+=s[i]
            i+=1
        return res

            