class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty. Cannot dequeue from an empty queue.")

# A. Enqueue five elements into the queue
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

# B. Dequeue three elements from the queue
try:
    dequeued_element1 = queue.dequeue()
    dequeued_element2 = queue.dequeue()
    dequeued_element3 = queue.dequeue()
    print("Dequeued elements:", dequeued_element1, dequeued_element2, dequeued_element3)
except IndexError as e:
    print(e)

# C. Check if the queue is empty
is_queue_empty = queue.is_empty()
print("Is the queue empty?", is_queue_empty)
