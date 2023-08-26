class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(data, node.left)
        else:
            return self._search_recursive(data, node.right)

    def delete(self, data):
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, node):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_recursive(data, node.left)
        elif data > node.data:
            node.right = self._delete_recursive(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._find_min(node.right)
                node.data = temp.data
                node.right = self._delete_recursive(temp.data, node.right)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def in_order_traversal(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" -> ")
            self.in_order_traversal(node.right)

    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

# a. Insert five elements into the tree
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)

# b. Search for a specific element in the tree
element_to_search = 30
is_element_found = bst.search(element_to_search)
print(f"Is {element_to_search} present in the tree? {is_element_found}")

# c. Delete an element from the tree
bst.delete(30)

# d. Print the tree using in-order traversal
print("In-Order Traversal of the tree:")
bst.in_order_traversal()
print("None")

# e. Find the height of the binary search tree
tree_height = bst.height()
print("Height of the binary search tree:", tree_height)
