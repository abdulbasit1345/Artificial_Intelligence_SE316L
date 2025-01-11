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


def bfs(graph, start, goal):
    open_list = deque([start])  # Queue for BFS
    closed_list = []           # Visited nodes

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

    print(f"Goal '{goal}' not found.")
    print("Open List:", list(open_list))
    print("Closed List:", closed_list)
    return closed_list


bfs(graph, start='A', goal='G')
