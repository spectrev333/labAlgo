from fontTools.misc.cython import returns
from LLBTreeNodeData import LLBTreeNodeData
from BTreeNode import BTreeNode
from LLIterator import LLIterator


class LLBTreeNode(BTreeNode):

    def __init__(self, key):
        super().__init__(key)
        self.chain = LLBTreeNodeData(self, key)

    def __iter__(self):
        return LLIterator(self.chain)

    def insert(self, data: LLBTreeNodeData):
        data.set_next(self.chain)
        self.chain = data