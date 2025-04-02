from BTreeNode import BTreeNode

class BTree:
    """
    A class representing a classic binary tree.
    """
    def __init__(self):
        self.root: BTreeNode = None

    def insert_key(self, key: int):
        self.insert(BTreeNode(key))

    def insert(self, node: BTreeNode):
        previous = None
        current = self.root
        while current is not None:
            previous = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.parent = previous
        if previous is None:
            self.root = node
        elif node.key < previous.key:
            previous.left = node
        else:
            previous.right = node

    def find(self, key):
        search_head = self.root
        while search_head is not None and search_head.key != key:
            if key < search_head.key:
                search_head = search_head.left
            else:
                search_head = search_head.right
        return search_head

    def find_all(self, key):
        search_head = self.root
        found_nodes = []
        while search_head is not None:
            if search_head.key == key:
                found_nodes.append(search_head)
                search_head = search_head.right
            elif key < search_head.key:
                search_head = search_head.left
            else:
                search_head = search_head.right
        return found_nodes

    def __str__(self):
        return " -> ".join(str(node) for node in self.inorder_traversal(self.root))

    def inorder_traversal(self, node):
        if node is not None:
            yield from self.inorder_traversal(node.left)
            yield node
            yield from self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node is not None:
            yield node
            yield from self.preorder_traversal(node.left)
            yield from self.preorder_traversal(node.right)