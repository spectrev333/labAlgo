from time import time
from typing import Callable
import networkx as nx
import matplotlib.pyplot as plt
from trees.BTree import BTree


def BTree_to_graphviz(tree):
    G = nx.DiGraph()
    node_positions = {}  # To store node positions for visualization

    def traverse(node, x=0.0, y=0, level=1, offset=1.5):
        if not node:
            return

        node_id = f"{node.key}_{id(node)}"
        G.add_node(node_id, label=str(node.key))
        node_positions[node_id] = (x, -y)  # Negative y for top-down drawing

        if node.left:
            left_id = f"{node.left.key}_{id(node.left)}"
            G.add_edge(node_id, left_id)
            traverse(node.left, x - offset / level, y + 1, level + 1, offset)

        if node.right:
            right_id = f"{node.right.key}_{id(node.right)}"
            G.add_edge(node_id, right_id)
            traverse(node.right, x + offset / level, y + 1, level + 1, offset)

    traverse(tree.root)
    return G, node_positions

def visualize(tree: BTree):
    plt.title('BTree vis')
    g, pos = BTree_to_graphviz(tree)
    labels = nx.get_node_attributes(g, 'label')

    nx.draw(g, pos, labels=labels, with_labels=True,
            node_size=1000, node_color="lightblue", edge_color="gray", font_size=12)

    plt.show()

def time_call(fun: Callable, args: tuple | list, times: int = 1):
    total = 0.0
    for i in range(times):
        start = time()
        fun(*args)
        end = time()
        total += (end - start)
    avg = total / times
    # print("avg exec time %0.3fs. (%d runs)" % (avg, times))
    return avg
