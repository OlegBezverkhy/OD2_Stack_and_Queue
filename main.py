# 1. Стеки
class  Stack:
    def __init__(self):
        self.items =[]

    def push(self,value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def print_stack(self):
        for item in self.items:
            print(item)


#2. Очередь
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def print_queue(self):
        for item in self.items:
            print(item)

#3. Дерево
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert (root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        print_tree(root.left, level + 1, "L--- ")
        print_tree(root.right, level + 1, "R--- ")


#4. Графы
class Graph:
    def __init__ (self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(node, '->', '->'.join(map(str, self.graph[node])))



# Проверка
# 1. Стек
print('Тест: Стеки')
stack = Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.is_empty())
print(stack.peek())
stack.print_stack()

# 2. Очередь
print('Тест: Очередь')
queue = Queue()
print(queue.is_empty())
queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")
queue.print_queue()
print(queue.is_empty())
print(queue.size())

# 3. Дерево:
print('Тест: Дерево')
root = Node(100)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 18)
root = insert(root, 30)
root = insert(root, 56)
root = insert(root, 89)
root = insert(root, 45)
root = insert(root, 60)
root = insert(root, 73)
root = insert(root, 98)
root = insert(root, 84)
print_tree(root)


# 4. Графы:
print('Тест: Графы')
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 5)
g.add_edge(0, 3)
g.add_edge(1, 1)
g.add_edge(1, 0)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()

