class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) !=  len(word2):
            return False
        count1, count2 = {},{}
        for i in range(len(word1)):
            count1[word1[i]] = count1.get(word1[i],0)+1
            count2[word2[i]] = count2.get(word2[i],0)+1
        return sorted(count1.values()) == sorted(count2.values()) and set(word1) == set(word2)