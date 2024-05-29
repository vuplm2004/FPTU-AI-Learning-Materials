# Function to create an adjacency list representation of the graph
def create_graph(vertices, edges):
    # Initialize an empty dictionary for the adjacency list
    graph = {}

    # Iterate over all the vertices and add an empty list for each vertex
    for vertex in vertices:
        graph[vertex] = []

    # Iterate over all the edges and add the adjacent vertices to the adjacency list
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    return graph

# Main program
if __name__ == '__main__':
    # Get input from user for vertices and edges
    print("Enter the vertices separated by spaces:")
    vertices = list(map(str, input().split()))

    print("Enter the edges (in the form 'u v') separated by spaces, one per line:")
    edges = []
    while True:
        try:
            edge = tuple(map(str, input().split()))
            edges.append(edge)
        except ValueError:
            break

    # Create the adjacency list representation of the graph
    graph = create_graph(vertices, edges)

    # Print the adjacency list representation of the graph
    print("Adjacency List Representation of the Graph:")
    for vertex in graph:
        print(vertex + " -> " + ", ".join(graph[vertex]))
        
# Function to find all possible paths in the graph from start to end using DFS
def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = dfs_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Main program
if __name__ == '__main__':
    # Get input from user for vertices and edges
    print("Enter the vertices separated by spaces:")
    vertices = list(map(str, input().split()))

    print("Enter the edges (in the form 'u v') separated by spaces, one per line:")
    edges = []
    while True:
        try:
            edge = tuple(map(str, input().split()))
            edges.append(edge)
        except ValueError:
            break

    # Create the adjacency list representation of the graph
    graph = create_graph(vertices, edges)

    # Get input from user for start and end vertices
    print("Enter the starting vertex:")
    start = input()
    print("Enter the destination vertex:")
    end = input()

    # Find all possible paths from start to end using DFS
    paths = dfs_paths(graph, start, end)

    # Print all the possible paths from start to end
    print("All possible paths from " + start + " to " + end + ":")
    for path in paths:
        print(" -> ".join(path))