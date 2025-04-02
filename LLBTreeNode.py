from fontTools.misc.cython import returns

from BTreeNode import BTreeNode

class LLBTreeNode(BTreeNode):

    def __init__(self, key):
        super().__init__(key)
        self.next = None
        self.i = self

    def __iter__(self):
        self.i = self
        return self

    def __next__(self):
        if self.i is None:
            raise StopIteration
        x = self.i
        self.i = self.i.next
        return x

    def set_next(self, next):
        self.next = next