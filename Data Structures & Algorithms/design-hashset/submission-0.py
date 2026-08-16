class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.hash_set = [[]] * self.size

    def get_idx(self, key):
        return key % self.size
        
    def add(self, key: int) -> None:
        idx = self.get_idx(key)
        if not self.contains(key):
            self.hash_set[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self.get_idx(key)
        if key in self.hash_set[idx]:
            self.hash_set[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self.get_idx(key)
        if key in self.hash_set[idx]:
            return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)