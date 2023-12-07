from collections import deque


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.matrix = []
        self.indexOfNodes = {}

        for i in range(len(nodes)):
            self.indexOfNodes[nodes[i]] = i

        for i in range(len(nodes)):
            row = [0] * len(nodes)
            self.matrix.append(row)
            
    def connectNodes(self, n1, n2):
        n1 = self.indexOfNodes[n1]
        n2 = self.indexOfNodes[n2]
        self.matrix[n1][n2] = 1
        self.matrix[n2][n1] = 1

    def bfs(self, startVal):
        visited = set()
        explorationQueue = deque([startVal])

        while explorationQueue:
            node = explorationQueue.popleft()
            if node not in visited:
                print((self.nodes[node]), end = ", ")
                visited.add(node)

                for neighbout, value in enumerate(self.matrix[node]):
                    if value ==1 and neighbout not in visited:
                        explorationQueue.append(neighbout)

    def displayMatrix(self):
        for row in self.matrix:
            print(row)

nodes = ["Nalgonda", "Khammam", "Seunderabad", "Karimnagar"]
graph = Graph(nodes)

graph.connectNodes("Nalgonda", "Khammam")
graph.connectNodes("Nalgonda", "Seunderabad")
graph.connectNodes("Nalgonda", "Karimnagar")
graph.connectNodes("Khammam", "Seunderabad")
graph.connectNodes("Khammam", "Karimnagar")
graph.connectNodes("Seunderabad", "Karimnagar")

# graph.displayMatrix()

print("Bfs as root place as nalgonda")
graph.bfs(1)
