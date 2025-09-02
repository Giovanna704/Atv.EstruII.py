import random

# Nó da Árvore
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

# Árvore Binária de Busca
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, valor):
        if self.root is None:
            self.root = Node(valor)
        else:
            self._insert(self.root, valor)

    def _insert(self, node, valor):
        if valor < node.valor:
            if node.left is None:
                node.left = Node(valor)
            else:
                self._insert(node.left, valor)
        else:
            if node.right is None:
                node.right = Node(valor)
            else:
                self._insert(node.right, valor)

    # Travessia In-Order (Esquerda, Raiz, Direita)
    def inorder(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node.left:
            self.inorder(node.left, result)
        result.append(node.valor)
        if node.right:
            self.inorder(node.right, result)
        return result

    # Travessia Pre-Order (Raiz, Esquerda, Direita)
    def preorder(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        result.append(node.valor)
        if node.left:
            self.preorder(node.left, result)
        if node.right:
            self.preorder(node.right, result)
        return result

    # Travessia Post-Order (Esquerda, Direita, Raiz)
    def postorder(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node.left:
            self.postorder(node.left, result)
        if node.right:
            self.postorder(node.right, result)
        result.append(node.valor)
        return result

    # Exibir a árvore (simplesmente em níveis)
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node.right:
            self.print_tree(node.right, level + 1)
        print("    " * level + str(node.valor))
        if node.left:
            self.print_tree(node.left, level + 1)


# ----------------- DEMONSTRAÇÃO -----------------
if __name__ == "__main__":
    print("\n=== ÁRVORE FIXA ===")
    bst_fixa = BinarySearchTree()
    valores_fixos = [55, 30, 80, 20, 45, 70, 90]
    for v in valores_fixos:
        bst_fixa.insert(v)

    bst_fixa.print_tree()
    print("In-Order:", bst_fixa.inorder())
    print("Pre-Order:", bst_fixa.preorder())
    print("Post-Order:", bst_fixa.postorder())

    print("\n=== ÁRVORE ALEATÓRIA ===")
    bst_rand = BinarySearchTree()
    valores_rand = random.sample(range(1, 100), 10)
    for v in valores_rand:
        bst_rand.insert(v)

    print("Valores inseridos:", valores_rand)
    bst_rand.print_tree()
    print("In-Order:", bst_rand.inorder())
    print("Pre-Order:", bst_rand.preorder())
    print("Post-Order:", bst_rand.postorder())
