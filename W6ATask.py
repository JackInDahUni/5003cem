class Graph(object):
    
	def __init__(self, size):
		self.adjMatrix = []
		for i in range(size):
			self.adjMatrix.append([0 for i in range(size)])
		self.size = size
		self.vertices = []

    #methods for (1) adding a vertex; (2) adding an edge; (3) removing an edge; and (4) printing the
    #matrix should appear here

	def addVertex(self):
		vertexName = chr(ord('1') + len(self.vertices))
		self.vertices.append(vertexName)
		self.size = len(self.vertices)
		for row in self.adjMatrix:
			row.append(0)
		self.adjMatrix.append([0] * self.size)

	def addEdge(self, vertex1, vertex2):
		edge1 = self.vertices.index(vertex1)
		edge2 = self.vertices.index(vertex2)
		self.adjMatrix[edge1][edge2] = 1
		self.adjMatrix[edge2][edge1] = 1
		
	def remEdge(self, vertex1, vertex2):
		edge1 = self.vertices.index(vertex1)
		edge2 = self.vertices.index(vertex2)
		self.adjMatrix[edge1][edge2] = 0
		self.adjMatrix[edge2][edge1] = 0

	def display_matrix(self):
		print(" ", end=" ")
		for vertex in self.vertices:
			print(vertex, end=" ")
		print()
		for i in range(self.size):
			print(self.vertices[i], end=" ")
			for j in range(self.size):
				print(self.adjMatrix[i][j], end=" ")
			print()




#remember list indexing - this is 1 out, unless we start the matrix at 0 (not a +ve integer)     
def main():
	g = Graph(4)
	for n in range(6):
		g.addVertex()
	g.addEdge('1','2')
	g.addEdge('4','5')
	g.addEdge('3','6')
	g.addEdge('4','1')
	g.addEdge('3','2')
	g.addEdge('2','3')
	g.addEdge('1','4')
	g.addEdge('6','5')

	g.display_matrix()
	g.remEdge('1','2')
	g.remEdge('6','5')
	g.display_matrix()
if __name__ == '__main__':
	main()
