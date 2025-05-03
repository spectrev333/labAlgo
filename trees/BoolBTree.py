from re import search

from trees.BTree import BTree
from trees.BoolBTreeNode import BoolBTreeNode

class BoolBTree(BTree):
    """
    A class representing a binary tree that balances on equal keys.
    """
    def __init__(self):
        super().__init__()
        self.root: BoolBTreeNode = None

    def insert_key(self, key: int):
        self.insert(BoolBTreeNode(key))

    def insert(self, node: BoolBTreeNode):
        previous = None
        current = self.root
        while current is not None:
            previous = current
            # if same key is found:
            # - go left if current.flag is false and toggle
            # - go right if current.flag is true and toggle
            if node.key == current.key:
                current.flag = not current.flag
                if not current.flag:
                    current = current.left
                else:
                    current = current.right
            elif node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.parent = previous
        if previous is None:
            self.root = node
        elif node.key == previous.key:
            # if inserting under a node with the same key:
            # - insert to the left if parent.flag is false
            # - insert to the right if parent.flag is true
            if not previous.flag:
                previous.left = node
            else:
                previous.right = node
        elif node.key < previous.key:
            previous.left = node
        else:
            previous.right = node

    def find_all(self, key):
        search_head = self.root
        found_nodes = []
        subtrees_to_be_searched = []
        while search_head is not None or len(subtrees_to_be_searched) != 0:
            if search_head is None:
                search_head = subtrees_to_be_searched.pop()
            elif search_head.key == key:
                found_nodes.append(search_head)
                subtrees_to_be_searched.append(search_head.left)
                search_head = search_head.right
            elif key < search_head.key:
                search_head = search_head.left
            else:
                search_head = search_head.right
        return found_nodes

