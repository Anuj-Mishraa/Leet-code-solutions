class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        blooming = defaultdict(int)                 # use line sweep
        for start, end in flowers:
            blooming[start] += 1
            blooming[end+1] -= 1

        ans, bloom_cnt = {}, 0
        h = sorted(people,reverse=True)            # sort persons desc so we can pop from last index
        for time in sorted(blooming.keys()):        # loop over sorted status updates
            bloom_change = blooming[time]
            while h and time > h[-1]:               # if current time is greater than
                ans[h.pop()] = bloom_cnt            # current person answer is last bloom_cnt
            if not h: break
            bloom_cnt += bloom_change

        return [ans[p] if p in ans else 0 for p in people]