class DirectedGraph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print(self.graph_dict)

    def get_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []

if __name__ == '__main__':
    routes = [
        ("Karachi", "Islamabad"),
        ("Islamabad", "Lahore"),
        ("Quetta", "Karachi"),
        ("Peshawar", "Quetta"),
        ("Karachi", "Peshawar"),
        ("Peshawar", "Lahore")
    ]

    route_graph = DirectedGraph(routes)