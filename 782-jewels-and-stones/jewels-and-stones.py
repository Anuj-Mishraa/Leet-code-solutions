class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_map = {j:0 for j in jewels}

        for s in stones:
            if s in jewel_map:
                jewel_map[s] += 1
        
        return sum(jewel_map.values())

        