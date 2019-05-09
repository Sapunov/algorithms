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


def left_descendant(node):
    '''Самая левая нода, начиная с node
    '''

    assert_node(node)

    if node.left is None:
        return node
    else:
        return left_descendant(node.left)


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

    def insert_all(self, keys):

        for key in keys:
            self.insert(key)

    def delete(self, node):

        assert_node(node)
        raise NotImplementedError()

    def next(self, node):

        assert_node(node)

        if node.has_right_child():
            return left_descendant(node.right)
        else:
            return right_ancestor(node)

    def find_range(self, left, right):

        result = []
        _, node = self._find_or_parent(left)

        while node and node.key <= right:
            if node.key >= left:
                result.append(node)
            node = self.next(node)

        return result

    def nearest_neighbour(self, node):

        assert_node(node)
        raise NotImplementedError()

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
