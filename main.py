from collections import Counter

from BTree import BTree
from BoolBTree import BoolBTree
from LLBTree import LLBTree
from LLBTreeNode import LLBTreeNode
from utils import BTree_to_graphviz, visualize
import networkx as nx
import time
import random
import matplotlib.pyplot as plt
import numpy as np

from TestDataGenerator import TestDataGenerator
from BTreeBench import BTreeBench

tree = LLBTree()

test_bench = BTreeBench(tree)

test_bench.run_all_and_plot(filter_outliers=True, average=False)
