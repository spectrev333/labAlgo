from collections import Counter

from BTree import BTree
from BoolBTree import BoolBTree
from LLBTree import LLBTree
from LLBTreeNode import LLBTreeNode
from utils import BTree_to_graphviz, visualize
import networkx as nx
import time
import random

from TestDataGenerator import TestDataGenerator

def bench(fun, times=1):
    total = 0.0
    for i in range(times):
        start = time.time()
        fun()
        end = time.time()
        total += (end - start)
    total /= times
    print("avg exec time %0.3fs. (%d runs)" % (total, times))


# tree = LLBTree()
#
# expected = 0
# start = time.time()
# for i in range((2**14)-1):
#     val = random.randint(1, 4)
#     tree.insert_key(val)
#     if val == 3:
#         expected += 1
# end = time.time()
#
# print("insertion took %0.3fs." % (end - start))
#
# #print(list(tree.preorder_traversal(tree.root)))
#
# print(tree.find_all(3))
# print(f"found {len(tree.find_all(3))}, expected {expected}")
#
# bench(lambda : tree.find_all(3), times=5)

tree = LLBTree()

tree.insert_key(10)
tree.insert_key(10)
tree.insert_key(10)
tree.insert_key(10)
tree.insert_key(10)
tree.insert_key(10)
tree.insert_key(10)

visualize(tree)

exit()

gen1 = TestDataGenerator(2**14, 0.90, 16380, (1, 3000))

data1 = gen1.generate_data_with_duplicates()

c = Counter(data1)

print(c)

btree = BTree()
boolbtree = BoolBTree()
llbtree = LLBTree()

print("insert")
#bench(lambda: list(btree.insert_key(d) for d in data1), times=3)
#bench(lambda: list(boolbtree.insert_key(d) for d in data1), times=3)
#bench(lambda: list(llbtree.insert_key(d) for d in data1), times=3)
for d in data1:
    #btree.insert_key(d)
    llbtree.insert_key(d)


print("\nsearch")

values_to_find = gen1.generate_search_keys(data1)

for value in values_to_find:
    #btree.find_all(value)
    llbtree.find_all(value)

#bench(lambda: list(btree.find_all(value) for value in values_to_find), times=3)
#bench(lambda: list(boolbtree.find_all(value) for value in values_to_find), times=3)
#bench(lambda: list(llbtree.find_all(value) for value in values_to_find), times=3)




