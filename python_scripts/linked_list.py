class Node:
    def __init__(self, value, connection = None):
        self.value = value
        self.connection = connection

    def __str__(self):
        return "Node(%s, %s)" % (self.value, self.connection)

class List:
    def __init__(self):
        self.root = None

    def prepend(self, value):
        self.root = Node(value, self.root)

    def append(self, value):
        if not self.root:
            self.prepend(value)
        else:
            last_idx = self.len() - 1
            i = 0
            node = self.root
            while i < last_idx:
                node = node.connection
                i += 1
            node.connection = Node(value)

    def at(self, idx):
        i = 0
        node = self.root
        while i < idx:
            node = node.connection
            i += 1
        return node.value

    def len(self):
        i = 0
        node = self.root
        while node:
            node = node.connection
            i += 1
        return i

    def last(self):
        return self.at(self.len() - 1)

    def __str__(self):
        node = self.root
        if node:
            memo = "List(%s" % node.value
        else:
            memo = "List("
        # node = node.connection
        while node:
            node = node.connection
            if node:
                memo += ", %s" % node.value
        memo += ")"
        return memo

list = List()
print(list)
list.append(3)
print(list)
list.append(1)
print(list)
list.append(4)
print(list)
list.append(1)
print(list)
list.append(5)
print(list)
