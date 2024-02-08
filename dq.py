# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class to implement Queue data structure
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return data
    def printLinkedList(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result

# Deque class to implement Deque data structure
class Deque:
    def __init__(self):
        self.head = None
        self.tail=None

    def add_front(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail=new_node

    def add_rear(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head=new_node
    
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    def printLinkedList(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result
    
    def remove_front(self):
        if self.head:
            removed_data = self.head.data
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
            return removed_data
        else:
            print("Error: The deque is empty.")
        return None
    
    def remove_rear(self):
        if self.head:
            removed_data = self.tail.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current_node = self.head
                while current_node.next != self.tail:
                    current_node = current_node.next
                current_node.next = None
                self.tail = current_node
            return removed_data
        else:
            print("Error: The deque is empty.")
        return None
    
    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

# Testing the Queue and Deque data structures
if __name__ == '__main__':
    # Creating a Queue
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue:")
    while not queue.is_empty():
        print(queue.dequeue())

    # Creating a Deque
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print("Deque:")
    while not deque.is_empty():
        print(deque.remove_front())