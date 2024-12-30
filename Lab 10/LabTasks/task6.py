import queue

max_priority_queue = queue.PriorityQueue()

# List of elements
elements = [4, 8, 1, 7, 3]

for element in elements:
    max_priority_queue.put(-element)

sorted_elements = []
while not max_priority_queue.empty():
    sorted_elements.append(-max_priority_queue.get())


print("Elements in max-priority queue:", sorted_elements)
