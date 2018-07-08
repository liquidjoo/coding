class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self._left_child = None
        self._right_child = None
        self.parent = None

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def left_child(self, node):

        # 현재 왼쪽 노드에 자식노드가 있다면 속성 해제
        if self._left_child:
            self._left_child.parent = None

        # 새 노드가 None이 아니라면 새 노드의 부모를 자신으로
        if node:
            node.parent = self
        self._left_child = node

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def right_child(self, node):
        if self._right_child:
            self._right_child.parent = None

        if node:
            node.parent = self
        self._right_child = node


    # 노드 infomation function
    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return self._right_child is None and self._right_child is None

    def is_left_child(self):
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        return self.parent and self.parent.right_child is self

    def has_left_child(self):
        return self._left_child is not None

    def has_right_child(self):
        return self._right_child is not None

    def has_both_child(self):
        return self._left_child is not None and self._right_child is not None

    def has_any_child(self):
        return not self.is_leaf()


p = TreeNode(4, 4)
l = TreeNode(2, 2)
p.left_child = l
print(l.parent.value)

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def put(self, key, val):
        if self.root:
            self.__put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

    def __put(self, key, val, current_node):
        target_node = current_node

        while True:
            if key < target_node.key:
                if not target_node.has_left_child():
                    target_node.left_child = TreeNode(key, val)
                    break
                else:
                    target_node = target_node.left_child

            else:
                if not target_node.has_right_child():
                    target_node.right_child = TreeNode(key, val)
                else:
                    target_node = target_node.right_child
        self.length += 1

    def get(self, key):
        if self.root is None:
            return None

        res = self.__get(key, self.root)
        if res:
            return res.value

        return None

    def __get(self, key, current_node):
        target_node = current_node

        while True:
            if key == target_node.key:
                return target_node

            elif key < target_node.key:
                if target_node.has_left_child:
                    target_node = target_node.left_child
                else:
                    return None

            else:
                if target_node.has_right_child:
                    target_node = target_node.right_child
                else:
                    return None

    def delete(self, key):
        if self.length == 1 and self.root.key == key:
            self.root = None
            self.length = 0
        node_to_delete = self.get(key)
        if not node_to_delete:
            raise KeyError("There is no Node in the Tree")

        if node_to_delete.is_leaf():
            if node_to_delete.is_left_child():
                node_to_delete.parent.left_child = None
            else:
                node_to_delete.parent.right_child = None