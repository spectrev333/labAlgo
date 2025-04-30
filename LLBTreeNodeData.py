class LLBTreeNodeData:
    """
    A class for chained data in a LLBTreeNode
    """
    def __init__(self, head):
        self.next = None
        self.head = head

    def __iter__(self):
        current = self
        while current is not None:
            yield current
            current = current.next

    def __repr__(self):
        return f"{self.head}"

    def set_next(self, next):
        self.next = next