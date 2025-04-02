from BTree import BTree
from BoolBTree import BoolBTree
from LLBTree import LLBTree
from LLBTreeNode import LLBTreeNode
from utils import BTree_to_graphviz, visualize
import networkx as nx

tree = LLBTree()

tree.insert_key(13)
tree.insert_key(14)
tree.insert_key(12)
tree.insert_key(15)
tree.insert_key(11)
tree.insert_key(9)
tree.insert_key(11)
tree.insert_key(11)
tree.insert_key(13)
tree.insert_key(11)
tree.insert_key(13)
tree.insert_key(11)
tree.insert_key(9)
tree.insert_key(11)
tree.insert_key(11)

print(list(tree.preorder_traversal(tree.root)))

print(tree.find_all(9))

#visualize(tree)


