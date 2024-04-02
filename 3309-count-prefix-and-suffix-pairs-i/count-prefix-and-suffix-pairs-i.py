class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if self.isPrefixAndSuffix(words[i],words[j]):
                    ans+=1
        return ans
    

    def isPrefixAndSuffix(self,str1,str2):
        if len(str2)<len(str1):
            return False
        p = str2[:len(str1)]
        s = str2[-len(str1):]
        if str1==p and str1==s:
            return True
        return False


        