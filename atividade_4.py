import random
from graphviz import Digraph

# -----------------------------
# Classe Nó da AVL
# -----------------------------
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# -----------------------------
# Classe AVL Tree
# -----------------------------
class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    # -----------------------------
    # Visualização com Graphviz
    # -----------------------------
    def export_graphviz(self, filename="avl_tree"):
        dot = Digraph(comment="Árvore AVL", format="png")
        dot.attr('node', shape='circle', style="filled", color="lightblue", fontname="Helvetica")

        def add_nodes_edges(node):
            if node:
                dot.node(str(node.key), f"{node.key}")
                if node.left:
                    dot.edge(str(node.key), str(node.left.key))
                    add_nodes_edges(node.left)
                if node.right:
                    dot.edge(str(node.key), str(node.right.key))
                    add_nodes_edges(node.right)

        add_nodes_edges(self.root)
        dot.render(filename, view=True)  # gera arquivo PNG e abre

# -----------------------------
# Demonstração
# -----------------------------
if __name__ == "__main__":
    print("\n=== Demonstração com valores fixos (rotações) ===")

    # Caso 1: [10, 20, 30]
    tree1 = AVLTree()
    for val in [10, 20, 30]:
        tree1.insert_key(val)
    tree1.export_graphviz("avl_fix1")

    # Caso 2: [10, 30, 20]
    tree2 = AVLTree()
    for val in [10, 30, 20]:
        tree2.insert_key(val)
    tree2.export_graphviz("avl_fix2")

    print("\n=== Demonstração com valores randômicos ===")
    tree3 = AVLTree()
    valores = random.sample(range(1, 100), 20)
    print("Inserindo:", valores)
    for val in valores:
        tree3.insert_key(val)
    tree3.export_graphviz("avl_random")
