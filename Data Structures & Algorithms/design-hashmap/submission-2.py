class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hash_map = [[]] * self.size

    def get_idx(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self.get_idx(key)
        self.hash_map[idx] = (key, value)
        
    def get(self, key: int) -> int:
        idx = self.get_idx(key)
        if self.hash_map[idx]:
            return self.hash_map[idx][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        idx = self.get_idx(key)
        if self.hash_map[idx] is not None:
            self.hash_map[idx] = []


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)