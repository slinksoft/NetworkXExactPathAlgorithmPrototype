
import networkx as nx

class MyGraph:
    def __init__(self):
        self.graph = nx.Graph()
        nodes = ['User1', 'S2', 'S3', 'S4', 'S5', 'S6', 'User2']
        self.graph.add_nodes_from(nodes)
        edges = [('User1', 'S2', {'delay': 10}), ('User1', 'S3', {'delay': 37}),
                ('S2', 'S4', {'delay': 24}), ('S3', 'S4', {'delay': 48}),
                ('S3', 'S6', {'delay': 96}), ('S4', 'S5', {'delay': 1}),
                ('S6', 'User2', {'delay': 84}), ('S5', 'User2', {'delay': 29})]
        self.graph.add_edges_from(edges)
        self._result = {}
        self._visit_limit = 1
        self._tDelay = 0;

    def get_nodes(self):
        return self.graph.nodes
    
    def get_edges(self):
        return self.graph.edges

    def DFS(self, total_delay, start, end):
        '''Obtain paths with total delays equal or close to the user's requirements.'''
        visits = {}
        self._tDelay = total_delay
        for node in G.get_nodes():
            visits[str(node)] = 0

        visits[start] = 1

        self._DFS2(total_delay, start, end, [], visits)
        return self._result

    def _DFS2(self, delay, curr, target, path, visits):
        if (curr == target and path != []):
            error = abs(delay) # The target was reached
            if not bool(self._result) or error < self._result["error"]:
                if (delay >= 0):
                    self._result = {"path":path.copy(), "error":error, "delay at": self._tDelay-error }
                else:
                    self._result = {"path":path.copy(), "error":error, "delay at": self._tDelay+error }
            return
        for neighbor in list(self.graph.neighbors(curr)):
            if (visits[str(neighbor)] < self._visit_limit):
                visits[str(neighbor)] += 1
                edge_delay = self.graph.edges[curr, neighbor]['delay']
                path.append((curr, neighbor)) # Found a potential path with this as the starting edge
                self._DFS2(delay - edge_delay, neighbor, target, path, visits)
                del path[-1] # Clean up after an end was reached (target or dead end)
                visits[str(neighbor)] -= 1

if __name__=="__main__":
    G = MyGraph()
    for node in G.get_nodes():
        print (node)

    for edge in G.get_edges().data():
        print (edge)

    result = G.DFS(total_delay=64, start="User1", end="User2")
    print("\nThe closest matching path is: ")
    print(f"| {result}")