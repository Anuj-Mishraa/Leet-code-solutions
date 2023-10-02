class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # AAABABB
        n = len(colors)
        i,a,b = 0,0,0
        while i<n:
            a1,b1 = 0,0
            while(i<n and colors[i]=='A'):
                a1+=1
                i+=1
            while(i<n and colors[i]=='B'):
                b1+=1
                i+=1
            if a1>2:
                a += a1-2
            if b1>2:
                b += b1-2
        return True if a>b else False
