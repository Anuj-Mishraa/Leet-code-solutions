class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        for i in range(0,len(letters)):
            if ord(letters[i]) > ord(target):
                return letters[i]
            
        return letters[0]