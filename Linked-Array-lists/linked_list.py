from node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self._author = 'JamesCunningham'

    def _findtail(self) -> Node:
        node = self.head

        while node.next is not None:
            node = node.next

        return node

        #recursively call nodes in the list untill you find on with the next value of: None, that node should be the "final" node in the list.

    def __repr__(self):
        if self.head is None:
            return '[]'
    
        s = '[' + str(self.head.item)
        node = self.head.next
        while node is not None:
            s += ', ' + str(node.item)
            node = node.next
    
        return s + ']'

    def __str__(self):
        return self.__repr__()

    def add(self, item):
        if self.head == None:
            self.head = Node(item, None)
        else:
            new = Node(item, None)
            self._findtail().next = new
    
    def clear(self):
        self.head = None

    def contains(self, search_value):
        node = self.head
        while node != None:
            if node.item == search_value:
                return True
            node = node.next
        return False
    
    def get(self, target):
        node = self.head
        i = 0
        while i < target:
            node = node.next
            i += 1

        return node.item
    
    def index_of(self, target):
        i = 0
        node = self.head
        while node != None:
            if node.item == target: return i
            node = node.next
            i += 1
        return -1
    
    def remove_at(self, target):
        if target == 0: self.head = self.head.next
        else:
            count = 0
            node = self.head
            while count < target-1:
                node = node.next
                count += 1
            node.next = node.next.next

    def set(self, target, target_value):
        count = 0
        node = self.head
        while count < target:
            node = node.next
            count += 1
        node.item = target_value

    def __len__(self):
        i = 0
        node = self.head
        while node != None:
            node = node.next
            i += 1
        return i
    
    def __eq__(self, other):
        if type(self) != type(other): return False
        if len(self) != len(other): return False

        node = self.head
        other_node = other.head

        while node != None:

            if node.item != other_node.item:
                return False
            
            node = node.next
            other_node = other_node.next

        return True
    
    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index == len(self):
            raise StopIteration
        item = self.get(self.iter_index)
        self.iter_index += 1
        return item