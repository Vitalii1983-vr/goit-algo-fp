import uuid  # Імпорт модуля uuid для генерації унікальних ідентифікаторів
import networkx as nx  # Імпорт бібліотеки networkx для роботи з графами
import matplotlib.pyplot as plt  # Імпорт бібліотеки matplotlib для візуалізації графів
from collections import deque  # Імпорт deque з модуля collections для реалізації черги в BFS

# Клас для представлення вузла бінарного дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Ліва дитина вузла
        self.right = None  # Права дитина вузла
        self.val = key  # Значення вузла
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для вузла

# Функція для додавання ребер до графа
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додавання вузла в граф
        if node.left:
            graph.add_edge(node.id, node.left.id)  # Додавання ребра до лівої дитини
            l = x - 1 / 2 ** layer  # Обчислення нової позиції для лівої дитини
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)  # Рекурсивне додавання ребер
        if node.right:
            graph.add_edge(node.id, node.right.id)  # Додавання ребра до правої дитини
            r = x + 1 / 2 ** layer  # Обчислення нової позиції для правої дитини
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)  # Рекурсивне додавання ребер
    return graph

# Функція для візуалізації дерева
def draw_tree(tree_root, colors_map=None):
    tree = nx.DiGraph()  # Створення спрямованого графа
    pos = {tree_root.id: (0, 0)}  # Початкова позиція для кореневого вузла
    tree = add_edges(tree, tree_root, pos)  # Додавання всіх ребер до графа

    if colors_map is None:
        colors_map = {}  # Якщо карта кольорів не задана, створюємо порожню
    colors = [colors_map.get(node[0], "skyblue") for node in tree.nodes(data=True)]  # Визначення кольорів вузлів
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Створення міток для вузлів

    plt.figure(figsize=(8, 5))  # Встановлення розміру фігури для графіка
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)  # Візуалізація графа
    plt.show()  # Показ графіка

# Функція для генерації кольорів
def generate_colors(n):
    return [f"#{hex(255 - i * 20)[2:]:0>2}0000" for i in range(n)]  # Генерація кольорів від темно-сірого до червоного

# Функція обходу в ширину (BFS)
def bfs(root):
    queue = deque([root])  # Ініціалізація черги з кореневого вузла
    visited = set()  # Множина для відвіданих вузлів
    color_index = 0  # Індекс для кольорів
    colors = generate_colors(100)  # Генерація 100 кольорів
    colors_map = {}  # Карта для збереження кольорів вузлів

    while queue:
        node = queue.popleft()  # Витяг вузла з черги
        if node and node.id not in visited:
            node.color = colors[color_index]  # Призначення кольору вузлу
            colors_map[node.id] = colors[color_index]  # Збереження кольору вузла в карту
            color_index += 1
            visited.add(node.id)  # Додавання вузла до відвіданих
            if node.left:
                queue.append(node.left)  # Додавання лівої дитини до черги
            if node.right:
                queue.append(node.right)  # Додавання правої дитини до черги
            draw_tree(heap_root, colors_map)  # Візуалізація дерева на кожному кроці

# Функція обходу в глибину (DFS)
def dfs(root):
    stack = [root]  # Ініціалізація стеку з кореневого вузла
    visited = set()  # Множина для відвіданих вузлів
    color_index = 0  # Індекс для кольорів
    colors = generate_colors(100)  # Генерація 100 кольорів
    colors_map = {}  # Карта для збереження кольорів вузлів

    while stack:
        node = stack.pop()  # Витяг вузла зі стеку
        if node and node.id not in visited:
            node.color = colors[color_index]  # Призначення кольору вузлу
            colors_map[node.id] = colors[color_index]  # Збереження кольору вузла в карту
            color_index += 1
            visited.add(node.id)  # Додавання вузла до відвіданих
            if node.right:
                stack.append(node.right)  # Додавання правої дитини до стеку
            if node.left:
                stack.append(node.left)  # Додавання лівої дитини до стеку
            draw_tree(heap_root, colors_map)  # Візуалізація дерева на кожному кроці

# Створення дерева
heap_root = Node(10)
heap_root.left = Node(5)
heap_root.right = Node(3)
heap_root.left.left = Node(0)
heap_root.left.right = Node(4)
heap_root.right.left = Node(1)

# Виконання BFS та DFS обходів і візуалізація
print("BFS:")
bfs(heap_root)

print("DFS:")
dfs(heap_root)
