class TimeMap:

    def __init__(self):
        self.hashmap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append([value, timestamp])
        else:
            self.hashmap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.hashmap.get(key, [])) - 1
        best_timestamp = ["", -1]

        while l <= r:
            mid = (l+r)//2
            if self.hashmap[key][mid][1] > timestamp:
                r = mid - 1
            elif self.hashmap[key][mid][1] <= timestamp:
                l = mid + 1
                if timestamp >= best_timestamp[1]:
                    best_timestamp = self.hashmap[key][mid]
        
        return best_timestamp[0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)