class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict ={}

        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] =  [end]
        print(self.graph_dict)

    def find_paths(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return None
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.find_paths(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths

    def find_path_shortest(self,start, end, path = []):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None
        shortest = None
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.find_path_shortest(node, end, path)
                if new_path:
                    if shortest is None or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest
    def find_path_longest(self,start, end, path = []):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None
        longest = None
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.find_path_shortest(node, end, path)
                if new_path:
                    if longest is None or len(new_path) > len(longest):
                        shortest = new_path
        return longest

if __name__ == '__main__':

        routes = [("Saint Louis","Chicago"),
                  ("Saint Louis","Ashburn"),
                  ("Chicago","Charlotte"),
                  ("San Diego", "Saint Louis"),
                  ("Austin", "San Diego"),
                  ("Ashburn","Chicago" ),
                  ]
        graph = Graph(routes)
        result = graph.find_paths("Saint Louis", "Charlotte")
        print(result)
        result = graph.find_path_longest("Saint Louis", "Charlotte")
        print(result)
        result = graph.find_path_shortest("Saint Louis","San Diego")
        print(result)
