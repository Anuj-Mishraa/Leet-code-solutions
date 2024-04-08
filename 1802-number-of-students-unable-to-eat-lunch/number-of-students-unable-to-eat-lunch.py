class Solution:
    def countStudents(self, st: List[int], sw: List[int]) -> int:
        counts = [0, 0]
        for student in st:
            counts[student] += 1

        remaining = len(sw)
        for sandwich in sw:
            if counts[sandwich] == 0:
                break
            if remaining == 0:
                break
            counts[sandwich] -= 1
            remaining -= 1
        
        return remaining