# graph storing structure
# source node -> [(dest_node , cost/distance)]


class Node:
    def __init__(self, distance, node):
        self.distance = distance
        self.node = node

def Dijkstra(graph,max_nodes):
    # Graph representation:
    # Source node 1: [(2, 50), (3, 30), (4, 100), (5, 10)]
    # Source node 3: [(2, 5)]
    # Source node 4: [(2, 20), (3, 50)]
    # Source node 5: [(4, 10)]

    # for source, adj_list in graph.items():
    #     print(f"Source node {source}: ", end="")
    #     for node in adj_list:
    #         print(f"({node.node}, {node.distance})", end=" ")
    #     print()
    pass

if __name__ == "__main__":
    graph = {}
    max_nodes = int(input("Enter max nodes (<= 5 preferable): "))
    for i in range(1, max_nodes + 1):
        max_adj_nodes = int(input(f"Max adjacent nodes for node {i} (enter 0 for no adjacent nodes): "))
        if max_adj_nodes == 0:
            continue
        elif max_adj_nodes >= max_nodes:
            print("Can't have more adjacent nodes than total graph nodes.")
            continue

        graph[i] = []
        for j in range(1, max_adj_nodes + 1):
            dest_node = int(input(f"Enter destination for source node {i}: "))
            dest_node_cost = int(input(f"Enter cost to destination node {dest_node}: "))
            graph[i].append(Node(distance=dest_node_cost, node=dest_node))
        print("\n")
    
    print("Graph representation:")
    for source, adj_list in graph.items():
        print(f"Source node {source}: ", end="")
        for node in adj_list:
            print(f"({node.node}, {node.distance})", end=" ")
        print()


    Dijkstra(graph,max_nodes)

    