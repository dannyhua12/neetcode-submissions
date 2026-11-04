class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.valMap = {}
        self.countMap = {}
        self.freqMap = defaultdict(OrderedDict)
        self.lfu = 0

    def count(self, key):
        cnt = self.countMap[key]
        self.countMap[key]+=1
        self.freqMap[cnt].pop(key)
        self.freqMap[cnt+1][key] = None

        if cnt == self.lfu and not self.freqMap[cnt]:
            self.lfu+=1
    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.count(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if key in self.valMap:
            self.count(key)
            self.valMap[key] = value
            return
        
        elif len(self.valMap) >= self.cap:
            lfukey, _  = self.freqMap[self.lfu].popitem(last=False)
            self.valMap.pop(lfukey)
            self.countMap.pop(lfukey)

        self.valMap[key] = value
        self.countMap[key] = 1
        self.freqMap[1][key] = None
        self.lfu = 1 


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)