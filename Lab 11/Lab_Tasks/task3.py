graph = {
    'A': ['B', 'E', 'C'],
    'B': ['E', 'D'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['D'],
    'F': [],
    'G': []
}


def dfs(graph, start, goal):
    open_list = [start]  # Stack for DFS
    closed_list = []  # Visited nodes

    while open_list:
        current_node = open_list.pop()  # Pop the last element (LIFO)
        if current_node in closed_list:
            continue

        closed_list.append(current_node)  # Mark it as visited

        # Check if we've reached the goal
        if current_node == goal:
            print(f"Goal '{goal}' found!")
            print("Open List:", open_list)
            print("Closed List:", closed_list)
            return closed_list

        # Add neighbors to the stack (in reverse order for correct DFS order)
        for neighbor in reversed(graph[current_node]):
            if neighbor not in closed_list:
                open_list.append(neighbor)

    print(f"Goal '{goal}' not found.")
    print("Open List:", open_list)
    print("Closed List:", closed_list)
    return closed_list


dfs(graph, start='A', goal='G')
