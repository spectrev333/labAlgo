from math import trunc

from BTree import BTree
from BTreeNode import BTreeNode
from LLBTreeNode import LLBTreeNode

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

            # attach previous parent to node
            node.parent = previous.parent
            if previous.parent is not None:
                if previous.parent.left == previous:
                    previous.parent.left = node
                else:
                    previous.parent.right = node

            # preserve left and right subtrees
            node.left = previous.left
            node.right = previous.right

            # append previous to node chain
            node.set_next(previous)

            # adjust child nodes
            if node.left is not None:
                node.left.parent = node
            if node.right is not None:
                node.right.parent = node
        elif node.key < previous.key:
            previous.left = node
        else:
            previous.right = node

    def find_all(self, key):
        return list(iter(self.find(key))) # abuse python iterators