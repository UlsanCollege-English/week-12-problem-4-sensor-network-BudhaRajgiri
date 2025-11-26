import heapq

def prim_mst(graph, start):
    """
    Compute the Minimum Spanning Tree (MST) of a weighted undirected graph using Prim's algorithm.
    Graph format: {node: [(neighbor, weight), ...]}
    Returns (mst_edges, total_cost):
        - mst_edges: list of (u, v, w) edges in the MST
        - total_cost: sum of weights of the MST
    """
    if start not in graph:
        return ([], 0)

    visited = set([start])
    mst_edges = []
    total_cost = 0
    edge_heap = []

    # Push all edges from the start node
    for neighbor, weight in graph[start]:
        heapq.heappush(edge_heap, (weight, start, neighbor))

    while edge_heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(edge_heap)
        if v in visited:
            continue
        # Add edge to MST
        visited.add(v)
        mst_edges.append((u, v, weight))
        total_cost += weight
        # Push all edges from the new node
        for neighbor, w in graph[v]:
            if neighbor not in visited:
                heapq.heappush(edge_heap, (w, v, neighbor))

    return (mst_edges, total_cost)