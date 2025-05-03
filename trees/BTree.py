from trees.BTreeNode import BTreeNode

class BTree:
    """
    A class representing a classic binary tree.
    """
    def __init__(self):
        self.root: BTreeNode = None

    def insert_key(self, key: int):
        """
        Creates a Tree node with desired key and does insertion
        :param key: desired key
        """
        self.insert(BTreeNode(key))

    def insert(self, node: BTreeNode):
        """
        Inserts a node in the tree
        :param node: node to be inserted
        """
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
        """
        Finds the first node in the tree matching the argument
        :param key: search argument
        :return: node if present
        """
        search_head = self.root
        while search_head is not None and search_head.key != key:
            if key < search_head.key:
                search_head = search_head.left
            else:
                search_head = search_head.right
        return search_head

    def find_all(self, key):
        """
        Finds all nodes matching the key
        :param key: search argument
        :return: List of nodes
        """
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
        """
        Recursive inorder traversal generator function
        :param node: start node
        :return: a generator yielding nodes following inorder traversal
        :raises: RecursionError: i the tree is too big
        """
        if node is not None:
            yield from self.inorder_traversal(node.left)
            yield node
            yield from self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        """
        Recursive preorder traversal generator function
        :param node: start node
        :return: a generator yielding nodes following preorder traversal
        :raises: RecursionError: i the tree is too big
        """
        if node is not None:
            yield node
            yield from self.preorder_traversal(node.left)
            yield from self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        """
        Recursive postorder traversal generator function
        :param node: start node
        :return: a generator yielding nodes following postorder traversal
        :raises: RecursionError: i the tree is too big
        """
        if node is not None:
            yield from self.postorder_traversal(node.left)
            yield from self.postorder_traversal(node.right)
            yield node