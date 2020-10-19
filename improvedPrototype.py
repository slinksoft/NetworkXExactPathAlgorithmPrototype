
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

    def get_nodes(self):
        return self.graph.nodes
    
    def get_edges(self):
        return self.graph.edges

    def DFS(self, total_delay, start, end, error):
        '''Obtain paths with total delays equal or close to the user's requirements.'''
        visits = {}
        for node in G.get_nodes():
            visits[str(node)] = 0

        visits[start] = 1

        self._DFS2(total_delay, start, end, [], error, visits)
        return self._result

    def _DFS2(self, delay, curr, target, path, error, visits):
        if (-error <= delay <= error and curr == target and path != []):
            key = abs(delay) # The target was reached
            if key in self._result:
                self._result[key].append(path.copy()) # Path must be copied or else it will get erased
            else:
                self._result[key] = [path.copy()]
            return
        if (delay <= -error):
            return # A dead end was reached
        for neighbor in list(self.graph.neighbors(curr)):
            if (visits[str(neighbor)] < 2):
                visits[str(neighbor)] += 1
                edge_delay = self.graph.edges[curr, neighbor]['delay']
                path.append((curr, neighbor)) # Found a potential path with this as the starting edge
                self._DFS2(delay - edge_delay, neighbor, target, path, error, visits)
                del path[-1] # Clean up after an end was reached (target or dead end)
                visits[str(neighbor)] -= 1

if __name__=="__main__":
    G = MyGraph()
    for node in G.get_nodes():
        print (node)

    for edge in G.get_edges().data():
        print (edge)

    t_delay = 64
    result = G.DFS(total_delay=t_delay, start="User1", end="User2", error=102)
    selectedKey = list(result.keys())[0];
    for key in result:
        if (key <= selectedKey and key != 0):
            selectedKey = key;
    print("\nThe closest path is: ")
    print(f"| {result.get(selectedKey)}")
    print(f"With delay being off by {selectedKey} of {t_delay}\n\n")
    for off_by, paths in result.items():
        if (off_by == 0):
            print(f"Exact path with delay of {t_delay}: ")
            for path in paths:
                print(f"| {path}")
