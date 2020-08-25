from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.result = None

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # create the new key with the vertex ID, and set the value to an empty set (no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # find vertex v1 in our vertices add v2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting_vertex
        # create an empty set to track visited verticies

        # while the queue is not empty:
        # get the current vertex (dequeue from queue)
        # print the current vertex
        # mark the current vertex as visited
        # add the current vertex to a visited_set
        # queue up all the current vertex's neighbors (so we can visit them next)

        # print the current vertex
        # queue up all the current vertex's neighbors (so we can visit them next)
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            v_last_vertex = v[-1]
            if v_last_vertex not in visited:
                if v_last_vertex == destination_vertex:
                    return v
                else:
                    visited.add(v_last_vertex)
                    for next_vert in self.get_neighbors(v_last_vertex):
                        v_copy = v[:]
                        v_copy.append(next_vert)
                        q.enqueue(v_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()

        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            v = s.pop()
            v_last = v[-1]
            if v_last not in visited:
                if v_last == destination_vertex:
                    return v
                else:
                    visited.add(v_last)
                    for next_vert in self.get_neighbors(v_last):
                        v_copy = v[:]
                        v_copy.append(next_vert)
                        s.push(v_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if self.result:
            return
        if visited is None:
            visited = set()
        if path is None:
            path = []
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            for child in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(
                    child, destination_vertex, path, visited)
                if new_path:
                    return new_path

        return None
