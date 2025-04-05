from BTree import BTree
from BoolBTree import BoolBTree
from LLBTree import LLBTree
from LLBTreeNode import LLBTreeNode
from utils import BTree_to_graphviz, visualize
import networkx as nx
import time
import random

def bench(fun, times=1):
    total = 0.0
    for i in range(times):
        start = time.time()
        fun()
        end = time.time()
        total += (end - start)
    total /= times
    print("avg exec time %0.3fs. (%d runs)" % (total, times))


tree = LLBTree()

expected = 0
start = time.time()
for i in range((2**14)-1):
    val = random.randint(1, 4)
    tree.insert_key(val)
    if val == 3:
        expected += 1
end = time.time()

print("insertion took %0.3fs." % (end - start))

#print(list(tree.preorder_traversal(tree.root)))

print(tree.find_all(3))
print(f"found {len(tree.find_all(3))}, expected {expected}")

bench(lambda : tree.find_all(3), times=5)

#visualize(tree)


