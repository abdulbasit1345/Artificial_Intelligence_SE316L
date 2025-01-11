graph = {
    'A': ['B', 'E', 'C'],
    'B': ['E', 'D'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['D'],
    'F': [],
    'G': []
}


def dfs_with_input(graph):
    start = input("Enter the initial state (start node): ").strip().upper()
    goal = input("Enter the goal state (end node): ").strip().upper()

    if start not in graph or goal not in graph:
        print("Invalid nodes. Please ensure the nodes exist in the graph.")
        return

    open_list = [start]  # Stack for DFS
    closed_list = []     # Visited nodes

    print("Open List: ", open_list)
    print("Closed List: ", closed_list)

    while open_list:
        current_node = open_list.pop()
        if current_node in closed_list:
            continue

        closed_list.append(current_node)  # Mark it as visited

        if current_node == goal:
            print(f"Goal '{goal}' found!")
            print("Open List:", open_list)
            print("Closed List:", closed_list)
            return closed_list

        # Add neighbors to the stack (in reverse order for correct DFS order)
        for neighbor in reversed(graph[current_node]):
            if neighbor not in closed_list:
                open_list.append(neighbor)
                print("Open List: ", open_list)
                print("Closed List: ", closed_list)

    print(f"Goal '{goal}' not found.")
    print("Open List:", open_list)
    print("Closed List:", closed_list)
    return closed_list

dfs_with_input(graph)
