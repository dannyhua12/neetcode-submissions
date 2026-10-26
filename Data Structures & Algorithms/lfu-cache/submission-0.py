
from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.valMap = {}      # key -> value
        self.countMap = {}    # key -> frequency
        self.freqMap = defaultdict(OrderedDict)  # frequency -> keys
        self.minFreq = 0

    def count(self, key):
        freq = self.countMap[key]

        # Remove key from its old frequency group
        del self.freqMap[freq][key]

        # Increase frequency
        self.countMap[key] += 1

        # Add key to its new frequency group
        newFreq = freq + 1
        self.freqMap[newFreq][key] = None

        # Update minimum frequency if needed
        if freq == self.minFreq and not self.freqMap[freq]:
            self.minFreq += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1

        self.count(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        # Existing key: update value and frequency
        if key in self.valMap:
            self.valMap[key] = value
            self.count(key)
            return

        # Cache full: remove LFU (LRU if tied)
        if len(self.valMap) >= self.cap:
            lfuKey, _ = self.freqMap[self.minFreq].popitem(last=False)
            del self.valMap[lfuKey]
            del self.countMap[lfuKey]

        # Insert new key with frequency 1
        self.valMap[key] = value
        self.countMap[key] = 1
        self.freqMap[1][key] = None
        self.minFreq = 1
