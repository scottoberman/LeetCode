from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.dict:
            if value == self.dict[key]:
                self.dict.move_to_end(key)
            else:
                self.dict.pop(key)
                self.dict[key] = value
        elif len(self.dict) == self.capacity:
            self.dict.popitem(False)
            self.dict[key] = value
        else:
            self.dict[key] = value
        

    def __str__(self):
        return str(self.dict)

#Test Data
test1 = (1, 1)
test2 = (2, 2)
test3 = (3, 3)
test4 = (4, 4)
cap = 2

runner = LRUCache(cap)
runner.put(*test1)
print(runner)
print(runner.get(2))
runner.put(*test2)
print(runner.get(2))
print(runner)
runner.put(*test3)
print(runner.get(2))
print(runner)
print(runner.get(2))
runner.put(*test4)
print(runner)

