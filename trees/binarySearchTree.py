class Node:

    def __init__(self, key, *, parent=None, left=None, right=None):

        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):

        return f'<Node:{self.key}>'


def assert_node(node):

    assert isinstance(node, Node), 'Node must be an instance of class Node'


class BinarySearchTree:

    def __init__(self, root_node=None):

        self.root = root_node

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

    def delete(self, node):

        assert_node(node)
        raise NotImplementedError()

    def next(self, node):

        assert_node(node)
        raise NotImplementedError()

    def find_range(self, left, right):

        raise NotImplementedError()

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
                if node.left is None:
                    return (False, node)
                node = node.left
            else:
                if node.right is None:
                    return (False, node)
                node = node.right

    def _right_ancestor(self, node):

        assert_node(node)
        raise NotImplementedError()

    def _left_descendant(self, node):

        assert_node(node)
        raise NotImplementedError()
