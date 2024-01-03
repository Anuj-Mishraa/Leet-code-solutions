class FreqStack:
    def __init__(self):
        self.ind = 0
        self.mp1 = defaultdict(list)
        self.mp = defaultdict(int)
        self.maxi = 0

    def push(self, val):
        self.mp[val] += 1
        self.maxi = max(self.maxi, self.mp[val])
        self.mp1[self.mp[val]].append(val)

    def pop(self):
        if not self.mp1[self.maxi]:
            return -1
        d = self.mp1[self.maxi].pop()
        self.mp[d] -= 1
        if not self.mp1[self.maxi]:
            self.maxi -= 1
        return d

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()