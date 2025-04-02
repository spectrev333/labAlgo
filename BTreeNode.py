class BTreeNode:
    """
    A class representing a node in a binary tree.

    Uses the @total_ordering to infer missing operators.
    """
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)

    def __eq__(self, other):
        if isinstance(other, BTreeNode):
            return self.key == other.key
        return False