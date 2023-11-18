import heapq


def longest_increasing_path(graph):
    def topological_sort(graph):
        in_degree = {node: 0 for node in graph}
        for node in graph:
            for neighbor, _ in graph[node]:
                in_degree[neighbor] += 1

        queue = [node for node in graph if in_degree[node] == 0]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current)
            for neighbor, _ in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return result

    sorted_nodes = topological_sort(graph)
    distances = {node: float("-inf") for node in graph}

    for node in sorted_nodes:
        for neighbor, weight in graph[node]:
            distances[neighbor] = max(distances[neighbor], distances[node] + 1)

    return max(distances.values())


# Example usage:
graph = {"A": [("B", 2), ("C", 3)], "B": [("D", 5)], "C": [("D", 7)], "D": []}

result = longest_increasing_path(graph)
print("Length of the longest increasing path:", result)
