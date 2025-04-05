class LLBTreeNodeData:
    """
    A class for chained data in a LLBTreeNode
    """
    def __init__(self, head):
        self.next = None
        self.iterator = self
        self.head = head

    def __iter__(self):
        self.iterator = self
        return self

    def __next__(self):
        if self.iterator is None:
            raise StopIteration
        x = self.iterator
        self.iterator = self.iterator.next
        return x

    def __repr__(self):
        return f"{self.head}"

    def set_next(self, next):
        self.next = next