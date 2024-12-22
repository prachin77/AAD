from flask import Flask, render_template, request, redirect, url_for
import heapq

app = Flask(__name__)

# Graph initialization (global)
graph = {}

def dijkstra(graph, start, destination):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priorityQueue = [(0, start)]
    previous_nodes = {node: None for node in graph}

    while priorityQueue:
        currentDistance, currentNode = heapq.heappop(priorityQueue)

        if currentDistance > distances[currentNode]:
            continue

        for neighbor, weight in graph[currentNode].items():
            distance = currentDistance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = currentNode
                heapq.heappush(priorityQueue, (distance, neighbor))

    # Build the shortest path
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    
    path.reverse()

    # If no valid path is found, return None
    if len(path) == 1 and path[0] != start:
        path = None
    
    return distances, path, previous_nodes

def generate_node_matrix(graph):
    """Generate a matrix representation of the graph with weights."""
    nodes = list(graph.keys())
    node_matrix = {}
    
    for node in nodes:
        node_matrix[node] = {}
        for neighbor in nodes:
            # Set infinity where no edge exists
            node_matrix[node][neighbor] = graph[node].get(neighbor, float('inf'))
    
    return node_matrix

def generate_dijkstra_matrix(graph, start):
    """Generate the final Dijkstra distance matrix for all nodes from the start."""
    distances, _, _ = dijkstra(graph, start, start)
    dijkstra_matrix = {}
    
    for node in graph:
        distances_from_node, _, _ = dijkstra(graph, node, node)
        dijkstra_matrix[node] = distances_from_node
    
    return dijkstra_matrix

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        newNode = request.form['newNode']
        newEdgeTo = request.form['newEdgeTo']
        edgeWeight = int(request.form['edgeWeight'])

        # Add edge to graph
        if newNode not in graph:
            graph[newNode] = {}
        
        graph[newNode][newEdgeTo] = edgeWeight
        
        if newEdgeTo not in graph:
            graph[newEdgeTo] = {}

        return redirect(url_for("index"))

    return render_template("index.html", graph=graph)

@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        start_node = request.form['startNode']
        destination_node = request.form['destinationNode']

        if start_node in graph and destination_node in graph:
            # Perform Dijkstra algorithm
            distances, path, _ = dijkstra(graph, start_node, destination_node)

            # Generate matrices
            node_matrix = generate_node_matrix(graph)
            dijkstra_matrix = generate_dijkstra_matrix(graph, start_node)

            # Prepare the result tables
            destination_table = [
                {'node': node, 'distance': distances[node] if distances[node] != float('inf') else '∞'}
                for node in graph
            ]

            return render_template("result.html", 
                                   graph=graph,
                                   node_matrix=node_matrix,
                                   dijkstra_matrix=dijkstra_matrix,
                                   start=start_node,
                                   destination=destination_node,
                                   distances=distances,
                                   path=path,
                                   destination_table=destination_table)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)