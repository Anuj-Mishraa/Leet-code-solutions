class Solution:
    def punishmentNumber(self, n: int) -> int:
        ret = 0
        for i in range(1, n+1):
            x = i * i
            s = str(x)
            m = len(s)
            found = False
            for mask in range(1 << (m-1)):
                val = 0
                cur = 0
                for j in range(m):
                    cur = cur * 10 + int(s[j])
                    if j + 1 == m or (mask >> j & 1):
                        val += cur
                        cur = 0
                if val == i:
                    found = True
                    break
            if found:
                ret += i*i
        return ret





        
