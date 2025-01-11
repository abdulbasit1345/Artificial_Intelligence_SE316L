from collections import deque

graph = {
    'A': ['B', 'E', 'C'],
    'B': ['E', 'D'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['D'],
    'F': [],
    'G': []
}


def bfs_with_input(graph):
    # Take user input for start and goal nodes
    start = input("Enter the initial state (start node): ").strip().upper()
    goal = input("Enter the goal state (end node): ").strip().upper()

    if start not in graph or goal not in graph:
        print("Invalid nodes. Please ensure the nodes exist in the graph.")
        return

    open_list = deque([start])  # Queue for BFS
    closed_list = []           # Visited nodes

    print("Open List: ", open_list)
    print("Closed List: ", closed_list)

    while open_list:
        current_node = open_list.popleft()
        closed_list.append(current_node)

        # Check if we've reached the goal
        if current_node == goal:
            print(f"Goal '{goal}' found!")
            print("Open List:", list(open_list))
            print("Closed List:", closed_list)
            return closed_list

        # Add neighbors to the open list if they haven't been visited
        for neighbor in graph[current_node]:
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)
                print("Open List: ", open_list)
                print("Closed List: ", closed_list)

    print(f"Goal '{goal}' not found.")
    print("Open List:", list(open_list))
    print("Closed List:", closed_list)
    return closed_list


bfs_with_input(graph)
