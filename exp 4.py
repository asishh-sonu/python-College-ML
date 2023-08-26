class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_reverse(self, node=None):
        if node is None:
            node = self.head
        if node is None:
            return
        self.print_reverse(node.next)
        print(node.data, end=" -> ")

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# A. Insert five elements at the beginning of the list
linked_list = SinglyLinkedList()
linked_list.insert_at_beginning(5)
linked_list.insert_at_beginning(4)
linked_list.insert_at_beginning(3)
linked_list.insert_at_beginning(2)
linked_list.insert_at_beginning(1)

# B. Delete an element from the list
linked_list.delete(3)

# C. Search for a specific element in the list
element_to_search = 4
is_element_found = linked_list.search(element_to_search)
print(f"Is {element_to_search} present in the list? {is_element_found}")

# D. Print the elements of the list in reverse order
print("Reversed List:")
linked_list.print_reverse()

# Print the elements of the list
print("Original List:")
linked_list.print_list()
