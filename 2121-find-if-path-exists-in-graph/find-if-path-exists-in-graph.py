class Solution:
    def validPath(self, n: int, e: List[List[int]], s: int, d: int) -> bool:
        return (f:=lambda v:v if p[v]==v else f(p[v]),p:=[*range(n)],any(setitem(p,f(u),f(v)) for u,v in e))[0](s)==f(d)