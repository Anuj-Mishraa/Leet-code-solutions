from sortedcontainers import SortedList
class NumberContainers:
    def __init__(self):
        self.mp = defaultdict(SortedList)
        self.mp1 = {}

    def change(self, ind, num):
        if ind in self.mp1:
            d = self.mp1[ind]
            self.mp[d].remove(ind)
        self.mp1[ind] = num
        self.mp[num].add(ind)
            

    def find(self, num):
        if num not in self.mp or not self.mp[num]:
            return -1
        return next(iter(self.mp[num]))


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)