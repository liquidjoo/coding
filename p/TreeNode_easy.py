class Node:
    def __init__(self, item):
        self.value = item
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self):
        self.root = Node(None)

    def add(self, item):
        if self.root.value is None:
            self.root.value = item
        else:
            self.__add(self.root, item)

    def __add(self, current_node, item):
        if current_node.value > item:
            if current_node.left_child is not None:
                self.__add(current_node.left_child, item)
            else:
                current_node.left_child = Node(item)

        else:
            if current_node.right_child is not None:
                self.__add(current_node.right_child, item)
            else:
                current_node.right_child = Node(item)

    def search(self, item):
        if self.root.value is None:
            return False
        else:
            self.__search(self.root, item)

    def __search(self, current_node, item):
        if current_node.value == item:
            return item
        else:
            if current_node.value > item:
                if current_node.left_child is not None:
                    return self.__search(current_node.left_child, item)
                else:
                    return False

            else:
                if current_node.right_child is not None:
                    return self.__search(current_node.right_child, item)
                else:
                    return False