class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        store = self.store[key]
        #store = [[1, 'foo'], [2, 'key']]
        l, r = 0, len(store)-1
        while l <= r:
            mid = (l + r)// 2
            if store[mid][0] == timestamp:
                return store[mid][1]
            elif store[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return '' if r < 0 else store[r][1]   #r will be the closest smaller answer and l will be closest bigger. if target < store[0][0] then r = -1 and l = 0. if target > store[-1][0], r = len(store)-1, l = len(store) and the loop breaks. use this logic to get things

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)