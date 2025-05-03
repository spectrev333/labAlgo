from trees.BTree import BTree
from trees.LLBTreeNode import LLBTreeNode


class LLBTree(BTree):
    """
    A class representing a binary tree, where duplicate nodes are chained.
    """
    def __init__(self):
        super().__init__()
        self.root: LLBTreeNode = None

    def insert_key(self, key: int):
        self.insert(LLBTreeNode(key))

    def insert(self, node: LLBTreeNode):
        previous = None
        current =  self.root
        is_duplicate = False
        while current is not None and not is_duplicate:
            previous = current
            if node.key == current.key:
                is_duplicate = True
            elif node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.parent = previous
        if previous is None:
            self.root = node
        elif is_duplicate: # node is same as previous
            previous.insert(node.chain)
        elif node.key < previous.key:
            previous.left = node
        else:
            previous.right = node

    def find_all(self, key):
        node = self.find(key)
        return node.chain