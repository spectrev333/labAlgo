from LLIterator import LLIterator


class LLBTreeNodeData:
    """
    A class for chained data in a LLBTreeNode
    """
    def __init__(self, head, value):
        self.next = None
        self.head = head
        self.value = value

    def __iter__(self):
        return LLIterator(self)

    def set_next(self, next):
        self.next = next