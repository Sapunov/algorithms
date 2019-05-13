import random


class Node:

    def __init__(self, key, *, parent=None, left=None, right=None):

        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def has_right_child(self):

        return self.right is not None

    def has_left_child(self):

        return self.left is not None

    def is_left_child(self):

        return self.parent and self.parent.left == self

    def is_right_child(self):

        return self.parent and self.parent.right == self

    def is_root(self):

        return not self.parent

    def has_any_children(self):

        return self.right or self.left

    def has_both_children(self):

        return self.right and self.left

    def __repr__(self):

        return f'<Node:{self.key}>'

    def __str__(self):

        return self.__repr__()


def assert_node(node):

    assert isinstance(node, Node), \
        f'Node must be an instance of class Node. Passed: {type(node)}'


def right_ancestor(node):

    assert_node(node)

    if node.parent is None:
        return None

    if node.key < node.parent.key:
        return node.parent
    else:
        return right_ancestor(node.parent)


def left_ancestor(node):

    assert_node(node)

    if node.parent is None:
        return None

    if node.key > node.parent.key:
        return node.parent
    else:
        return left_ancestor(node.parent)


class BinarySearchTree:

    def __init__(self, root_node=None):

        self.root = root_node
        self.size = 0

    def find(self, key):

        found, node = self._find_or_parent(key)

        if found:
            return node

        return None

    def insert(self, key):

        found, parent = self._find_or_parent(key)

        if not found:
            node = Node(key, parent=parent)
            if parent is not None:
                if parent.key > key:
                    parent.left = node
                else:
                    parent.right = node
            else:  # root node
                self.root = node
            self.size += 1

    def insert_all(self, keys, *, use_random=True):

        if use_random:
            random.shuffle(keys)

        for key in keys:
            self.insert(key)

    def delete(self, node):

        assert_node(node)

        self.size -= 1

        # Assign none by default to handle case when
        # node has no children
        new_parent_child = None

        if node.has_both_children():
            # Find next node
            next_node = self.next(node)
            # Assign left node to the new node
            node.left.parent = next_node
            next_node.left = node.left
            # Reassign child of the parent
            new_parent_child = next_node
            next_node.parent = node.parent
        elif node.has_any_children():
            child = node.left if node.has_left_child() else node.right
            child.parent = node.parent
            new_parent_child = child

        if node.is_left_child():
            node.parent.left = new_parent_child
        elif node.is_right_child():
            node.parent.right = new_parent_child
        else:
            self.root = new_parent_child

    def delete_by_key(self, key):

        node = self.find(key)
        if node:
            self.delete(node)

    def next(self, node):

        assert_node(node)

        if node.has_right_child():
            return self.min(node.right)
        else:
            return right_ancestor(node)

    def prev(self, node):

        assert_node(node)

        if node.has_left_child():
            return self.max(node.left)
        else:
            return left_ancestor(node)

    def find_range(self, left, right):

        result = []
        _, node = self._find_or_parent(left)

        while node and node.key <= right:
            if node.key >= left:
                result.append(node)
            node = self.next(node)

        return result

    def nearest_neighbour(self, key):

        found, node = self._find_or_parent(key)

        if found:
            return (self.prev(node), self.next(node))
        elif node.key < key:
            return (node, self.next(node))
        else:
            return (self.prev(node), node)

    def dfs(self, func):

        if self.root is None:
            return

        stack = [self.root]

        while stack:
            node = stack.pop()
            func(node)
            if node.has_right_child():
                stack.append(node.right)
            if node.has_left_child():
                stack.append(node.left)

    def bfs(self, func):

        if self.root is None:
            return

        stack = [self.root]

        while stack:
            node = stack.pop(0)
            func(node)
            if node.has_left_child():
                stack.append(node.left)
            if node.has_right_child():
                stack.append(node.right)

    def max(self, node=None):

        if node is None:
            node = self.root

        if node is None:
            return None

        while node.has_right_child():
            node = node.right

        return node

    def min(self, node=None):

        if node is None:
            node = self.root

        if node is None:
            return None

        while node.has_left_child():
            node = node.left

        return node

    def keys(self):

        keys = []
        self.inorder(lambda node: keys.append(node.key))

        return keys

    def inorder(self, func):

        root = self.root

        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                func(root)
                root = root.right

    def _find_or_parent(self, key):

        node = self.root

        if node is None:
            return (False, None)

        while True:
            if node.key == key:
                return (True, node)
            if node.key > key:
                if not node.has_left_child():
                    return (False, node)
                node = node.left
            else:
                if not node.has_right_child():
                    return (False, node)
                node = node.right

    def __repr__(self):

        return f'<BST: root={self.root} size={self.size}>'

    def __str__(self):

        return self.__repr__()


def print_as_list(node):

    print(f'{node} -> {node.left}, {node.right}')
