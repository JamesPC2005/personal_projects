from ctypes import resize


class ArrayList:

    def __init__(self):
        self.size = 0
        self.list = [None]*100
        self._author = 'JamesCunningham'

    def __repr__(self):
        if self.size == 0: return '[]'
        s = '[' + str(self.list[0])
        i = 1
        while i < self.size:
            s += ', ' + str(self.list[i])
            i += 1
        return s + ']'

    def __str__(self):
        return self.__repr__()
        
    def add(self, item):
        if self.size == len(self.list): self._resize(len(self.list) * 2)
        self.list[self.size] = item
        self.size += 1
    
    def _resize(self, new_size):
        new_list = [None] * new_size
        for i in range(self.list):
            new_list[i] = self.list[i]
        self.list = new_list

    def clear(self):
        self.size = 0

    def contains(self, search_value):
        i = 0
        while i < self.size:
            if self.list[i] == search_value:
                return True
            i += 1
        return False
    
    def get(self, target):
        return self.list[target]
    
    def index_of(self, target):
        i = 0
        while i < self.size:
            if self.list[i] == target: return i
            i += 1
        return -1
    
    def remove_at(self, target):
        i = target
        while i < self.size - 1:
            self.list[i] = self.list[i+1]
            i += 1
        self.size -= 1
        # self.size -= 1
        # if target == 0:
        #     self.list = self.list[1 : len(self.list)]
        # elif target == len(self.list):
        #     self.list = self.list[0 : len(self.list) - 1]
        # else:
        #     self.list = self.list[0 : target : len(self.list)]

    def set(self, target, target_value):
        self.list[target] = target_value

    def __len__(self):
        return self.size
    
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        i = 0
        while i < self.size:
            if self.list[i] != other.list[i]:
                return False
            i += 1
        return True
        

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index == self.size:
            raise StopIteration
        item = self.list[self.iter_index]
        self.iter_index += 1
        return item