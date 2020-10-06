import networkx as nx
import matplotlib.pyplot as plt

class TheGraph:
	graph = nx.Graph()
	graph.add_nodes_from(['UserA' ,'UserB', 'UserC','S1','S2','S3','S4','S5','S6','S7', 'S8'])
	edges = [('UserA' , 'S1', {'delay': 3}),
			('UserA' , 'S8', {'delay': 8}),
			('S1', 'S3', {'delay': 10}),
			('S3', 'S5', {'delay': 12}),
			('S2', 'S4', {'delay': 2}),
			('S3', 'S2', {'delay': 9}),
			('S3', 'S6', {'delay': 8}),
			('S4', 'S5', {'delay': 12}),
			('S3', 'S6', {'delay': 15}),
			('S5', 'UserB', {'delay': 4}),
			('S2', 'UserB', {'delay': 5}),
			('S6', 'S8', {'delay': 7}),
			('S7', 'S8', {'delay': 7}),
			('S6', 'S4', {'delay': 7}),
			('S7', 'UserC', {'delay': 4}),
			('S4', 'UserC', {'delay': 8})]

	graph.add_edges_from(edges)

	def get_nodes(self):
		return self.graph.nodes

	def get_edges(self):
		return self.graph.edges

	def DFS(self, curr_delay, total_delay, start, end):
			'''Obtain paths with total delays equal to the user's requirements.'''
			return self._DFS(curr_delay, total_delay, start, end, [])


	def _DFS(self, cDelay, tDelay, curr, target, path):
			if (curr == target):
				if (cDelay == 0):
					# The target is reached
					print("Exact path @ " + str(tDelay) + ":")
					print (path)
					return
				elif (cDelay <= 0 or cDelay >= 0):
					# A dead end was reached
					if (cDelay >= -5 and cDelay <= 0):
						print("Path close to delay of " + str(tDelay) + " @ " + str(tDelay+abs(cDelay)) + " :")
						print(path)
						return
					elif (cDelay >= 0 and cDelay <= 5):
						print("Path close to delay of " + str(tDelay) + " @ " + str(tDelay-cDelay) + " :")
						print(path)
						return
			elif (cDelay <= 0):
				return
			for neighbor in list(self.graph.neighbors(curr)):
				edge_delay = self.graph.edges[curr, neighbor]['delay']
				path.append((curr, neighbor)) # Found a potential path with this as the starting edge
				self._DFS(cDelay - edge_delay, tDelay, neighbor, target, path)
				path.remove((curr, neighbor)) # Clean up after an end was reached (target or dead end)


if __name__=="__main__":
	G = TheGraph()
	delay = 29; # desired delay
	G.DFS(curr_delay=delay, total_delay=delay, start="UserA", end="UserB")