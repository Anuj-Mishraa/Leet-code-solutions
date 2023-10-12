class Solution:
    def insert(self, vals: List[List[int]], nt: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(vals)):
            if nt[1]<vals[i][0]:
                res.append(nt)
                return res+vals[i:]
            elif nt[0]>vals[i][1]:
                res.append(vals[i])
            else:
                nt = [min(vals[i][0],nt[0]),max(vals[i][1],nt[1])]
        res.append(nt)
        return res



            
        