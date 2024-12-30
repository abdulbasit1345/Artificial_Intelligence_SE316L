import queue

lifo_queue = queue.LifoQueue()

lifo_queue.put(12)
lifo_queue.put(25)
lifo_queue.put(67)

print("Items in LIFO Queue:")
while not lifo_queue.empty():
    print(lifo_queue.get())
