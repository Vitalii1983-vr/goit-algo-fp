import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Ліва дитина
        self.right = None  # Права дитина
        self.val = key  # Значення вузла
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додавання вузла в граф
        if node.left:
            graph.add_edge(node.id, node.left.id)  # Додавання лівої дитини як ребро
            l = x - 1 / 2 ** layer  # Позиція лівої дитини
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)  # Додавання правої дитини як ребро
            r = x + 1 / 2 ** layer  # Позиція правої дитини
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)]  # Використання значень вузлів як міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def heapify(arr, n, i):
    largest = i  # Ініціалізуємо найбільший як корінь
    l = 2 * i + 1  # Ліва дитина
    r = 2 * i + 2  # Права дитина

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def array_to_tree(arr):
    nodes = [Node(key) for key in arr]
    for i in range(len(nodes)):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0] if nodes else None

# Приклад використання
arr = [10, 20, 15, 30, 40]  # Масив для побудови купи
build_heap(arr)  # Побудова купи з масиву
root = array_to_tree(arr)  # Перетворення масиву в дерево

draw_tree(root)  # Візуалізація дерева
