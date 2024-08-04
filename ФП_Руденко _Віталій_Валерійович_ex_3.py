import heapq  # Імпорт модуля heapq для роботи з пріоритетною чергою

class Graph:
    def __init__(self):
        # Ініціалізація графа як словника для зберігання списків суміжності
        self.edges = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Додавання ребра від from_node до to_node з певною вагою
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))
        
        # Для неорієнтованого графа додаємо ребро в обох напрямках
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[to_node].append((from_node, weight))

def dijkstra(graph, start):
    # Ініціалізація відстаней: відстань до стартової вершини дорівнює 0, до інших - нескінченність
    distances = {vertex: float('infinity') for vertex in graph.edges}
    distances[start] = 0

    # Ініціалізація пріоритетної черги з початковою вершиною
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Вибираємо вершину з мінімальною відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропускаємо вершини, які вже оброблені з коротшою відстанню
        if current_distance > distances[current_vertex]:
            continue
        
        # Оновлюємо відстані до сусідів поточної вершини
        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight
            
            # Якщо нова відстань коротша, оновлюємо і додаємо в чергу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Створення графа
graph = Graph()
graph.add_edge('A', 'B', 5)  # Додаємо ребро між вершинами A і B з вагою 5
graph.add_edge('A', 'C', 10)  # Додаємо ребро між вершинами A і C з вагою 10
graph.add_edge('B', 'D', 3)  # Додаємо ребро між вершинами B і D з вагою 3
graph.add_edge('C', 'D', 2)  # Додаємо ребро між вершинами C і D з вагою 2
graph.add_edge('D', 'E', 4)  # Додаємо ребро між вершинами D і E з вагою 4

# Виконання алгоритму Дейкстри
start_vertex = 'A'  # Визначаємо стартову вершину
shortest_paths = dijkstra(graph, start_vertex)  # Обчислюємо найкоротші шляхи від стартової вершини

# Виведення результатів
for vertex, distance in shortest_paths.items():
    # Виводимо найкоротші відстані від стартової вершини до кожної вершини
    print(f"Відстань від {start_vertex} до {vertex} дорівнює {distance}")
