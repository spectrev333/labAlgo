from BTreeNode import BTreeNode

class BoolBTreeNode(BTreeNode):
    """
    A class representing a node in a binary tree that balances equal keys.
    """

    def __init__(self, key):
        super().__init__(key)
        self.flag = False