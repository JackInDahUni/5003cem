from collections import defaultdict
import sys

class Graph():
    def __init__(self, size):
        # Initialize the graph with a defaultdict to store connected nodes and a dictionary to store edge weights
        self.edges = defaultdict(list)      # dictionary of all connected nodes, e.g., {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights = {}                   # dictionary of edges and weights, e.g., {('X', 'A'): 7, ('X', 'B'): 2, ...}
        self.size = size                    # size of the graph
        self.dist = []                      # list to store the distances from the start node
        for i in range(size):
            self.dist.append(sys.maxsize)   # Initialize distances to maximum value (infinity)
        self.previous = []                  # list to store previous nodes in the shortest path
        for i in range(size):
            self.previous.append(None)     # Initialize previous nodes as None

    # Method to add an edge to the graph (bidirectional)
    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)    # Add 'to_node' to the list of connected nodes for 'from_node'
        self.edges[to_node].append(from_node)    # Add 'from_node' to the list of connected nodes for 'to_node'
        self.weights[(from_node, to_node)] = weight  # Assign weight to the edge (from_node, to_node)
        self.weights[(to_node, from_node)] = weight  # Assign weight to the edge (to_node, from_node)

    # Method to find the smallest node based on distance
    def findSmallestNode(self): 
        smallest = self.dist[self.getIndex(self.Q[0])]    # Initialize smallest distance with the first node's distance
        result = self.getIndex(self.Q[0])                  # Initialize result with the index of the first node
        for i in range(len(self.dist)):
            if self.dist[i] < smallest:
                node = self.unpoppedQ[i]                   # Get the node corresponding to the current index
                if node in self.Q:                         # Check if the node is still in the unvisited nodes
                    smallest = self.dist[i]                # Update smallest distance if a smaller one is found
                    result = self.getIndex(node)           # Update result with the index of the current node
        return result

    # Method to get the index of a node in the list of unvisited nodes
    def getIndex(self, neighbour):
        for i in range(len(self.unpoppedQ)):
            if neighbour == self.unpoppedQ[i]:
                return i

    # Method to get the position of a node in the list of visited nodes
    def getPopPosition(self, uNode):
        result = 0
        for i in range(len(self.Q)):
            if self.Q[i] == uNode:
                return i
        return result

    # Method to get unvisited neighbor nodes of a given node
    def getUnvisitedNodes(self, uNode):
        resultList = []
        allNeighbours = self.edges[uNode]
        for neighbour in allNeighbours:
            if neighbour in self.Q:
                resultList.append(neighbour)
        return resultList          

    # Dijkstra's algorithm implementation
    def dijsktra(self, start, end):                                
        self.Q = []                                # Initialize the list of unvisited nodes
        for key in self.edges:
            self.Q.append(key)                     # Add all nodes to the list of unvisited nodes
        for i in range(len(self.Q)):
            if self.Q[i] == start:
                self.dist[i] = 0                   # Set distance of start node to 0
        self.unpoppedQ = self.Q[0:]                # Make a copy of the list of unvisited nodes

        while self.Q:                              # Loop until all nodes are visited
            u = self.findSmallestNode()            # Find the node with the smallest distance
            if self.dist[u] == sys.maxsize:
                break                             # If smallest distance is infinity, break the loop
            if self.unpoppedQ[u] == end:
                break                             # If the end node is reached, break the loop

            uNode = self.unpoppedQ[u]              # Get the node corresponding to the index
############################################################################
            for vNode in self.getUnvisitedNodes(uNode):   # Update the distance of the neighbor nodes
                alt = self.dist[u] + self.weights[(uNode, vNode)]   # Calculate the distance from start node to vNode through uNode
                if alt < self.dist[self.getIndex(vNode)]:   # If distance is less than current distance for vNode, update it
                    self.dist[self.getIndex(vNode)] = alt
                    self.previous[self.getIndex(vNode)] = uNode   # Record uNode as previous node for vNode
            self.Q.remove(uNode)                              # Remove the current node from list of unvisited nodes
############################################################################
        shortest_path = []                                   # List to store the shortest path
        shortest_path.insert(0, end)                         # Insert the end node at the beginning of the path
        u = self.getIndex(end)                               # Get the index of the end node
        while self.previous[u] != None:
            shortest_path.insert(0, self.previous[u])        # Insert previous nodes into the path
            u = self.getIndex(self.previous[u])
############################################################################
        cost = self.dist[self.getIndex(end)]                 # Calculate the value of the shortest path
############################################################################

        return shortest_path, cost

# Create a graph object with 8 nodes
graph = Graph(8)

# Define edges and their weights
edges = [
    ('O', 'A', 2),
    ('O', 'B', 5),
    ('O', 'C', 4),
    ('A', 'B', 2),
    ('A', 'D', 7),
    ('A', 'F', 12),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('B', 'E', 3),
    ('C', 'E', 4),
    ('D', 'E', 1),
    ('D', 'T', 5),
    ('E', 'T', 7),
    ('F', 'T', 3),
]

# Add edges to the graph
for edge in edges:
    graph.add_edge(*edge)

# Test Dijkstra's algorithm with different start and end nodes
print(graph.dijsktra('O', 'T'))
print(graph.dijsktra('A', 'E'))
print(graph.dijsktra('F', 'C'))
