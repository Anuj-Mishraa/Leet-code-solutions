class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False 
        if len(s)==len(t) and s!=t:
            return False
        if len(s)==0 and len(s)!=0:
            return False
        if len(s)==0 and len(s)==0:
            return True
        st = []
        for i in s:
            st.append(i)
        for i in t[::-1]:
            if st and i==st[-1]:
                st.pop()
        return (len(st)==0)
        
