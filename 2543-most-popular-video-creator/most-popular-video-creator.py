import sys
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        mp = {}
        mx_v = -1
        for i in range(len(creators)):
            if creators[i] not in mp:
                mp[creators[i]] = [views[i],ids[i],views[i]]
            else:
                mp[creators[i]][0]+=views[i]
                if mp[creators[i]][2]<views[i]:
                    mp[creators[i]][1] = ids[i]
                    mp[creators[i]][2] = views[i]
                elif mp[creators[i]][2]==views[i]:
                    mp[creators[i]][1] = min(mp[creators[i]][1],ids[i])
            mx_v = max(mx_v,mp[creators[i]][0])
        ans = []
        for i in mp:
            if mp[i][0]==mx_v:
                ans.append([i,mp[i][1]])
        return ans


