class Graph(object):
    
	def __init__(self, size):
		self.adjMatrix = []
		for i in range(size):
			self.adjMatrix.append([0 for i in range(size)])
		self.size = size
		self.vertices = []

    #methods for (1) adding a vertex; (2) adding an edge; (3) removing an edge; and (4) printing the
    #matrix should appear here
														# Generate a new vertex name based on the current number of vertices
														# The vertex names are represented as characters starting from '1' for the first vertex,
	def addVertex(self):									# '2' for the second, and so on
		vertexName = chr(ord('1') + len(self.vertices))
		self.vertices.append(vertexName)					# Append the new vertex name to the list of vertices
		self.size = len(self.vertices)						# Update the size of the graph (number of vertices)
		for row in self.adjMatrix:							# Add a new column (initialized with zeros) to each row in the adjacency matrix
			row.append(0)									# This prepares the matrix for the new vertex by adding a new entry for each existing vertex
		self.adjMatrix.append([0] * self.size)				# Add a new row (initialized with zeros) to the adjacency matrix to represent the new vertex			
															# This adds a new row to the matrix to accommodate the new vertex and initializes its connections to other vertices as zeros
	def addEdge(self, vertex1, vertex2):
		edge1 = self.vertices.index(vertex1)				# Find the indices of the vertices in the vertices list
		edge2 = self.vertices.index(vertex2)				# This step retrieves the positions (indices) of the vertices in the list of vertices
		self.adjMatrix[edge1][edge2] = 1    				# Set the corresponding entry in the adjacency matrix to 1 to represent the edge
		self.adjMatrix[edge2][edge1] = 1    				# This step updates the adjacency matrix to represent the connection between the two vertices

	def remEdge(self, vertex1, vertex2):
		edge1 = self.vertices.index(vertex1)				# Find the indices of the vertices in the vertices list
		edge2 = self.vertices.index(vertex2)				# This step retrieves the positions (indices) of the vertices in the list of vertices
		self.adjMatrix[edge1][edge2] = 0					# Set the corresponding entry in the adjacency matrix to 0 to remove the edge
		self.adjMatrix[edge2][edge1] = 0					# This step updates the adjacency matrix to remove the connection between the two vertices

	def display_matrix(self):
		print(" ", end=" ")									# Print the header row with vertex labels
		for vertex in self.vertices:
			print(vertex, end=" ")
		print()
															# Print a horizontal line below the header row
		print(("  ")+("-" * (len(self.vertices) * 2 - 1)))	# This line separates the header row from the matrix contents for better readability
		for i in range(self.size):							# Print the adjacency matrix
			print(self.vertices[i], end="|")				# Print the vertex label for each row followed by a separator '|'
			for j in range(self.size):						# Print the values from the adjacency matrix for the current row
				print(self.adjMatrix[i][j], end=" ")
			print()											# Move to the next line after printing all values for the current row




#remember list indexing - this is 1 out, unless we start the matrix at 0 (not a +ve integer)     
def main():
	g = Graph(4)
	for n in range(7):
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
