class Node:

    def __init__(self, key, *, parent=None, left=None, right=None):

        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

        self.height = 0
        self.recompute_height()

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

    def recompute_height(self):

        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0

        self.height = 1 + max(left_height, right_height)

    def __repr__(self):

        return f'<Node:{self.key}|{self.parent.key if self.parent else None}>'

    def __str__(self):

        return self.__repr__()


def assert_node(node):

    assert isinstance(node, Node), \
        f'Node must be an instance of class Node. Passed: {type(node)}'


class AVLTree:

    def __init__(self):

        self.root = None
        self.size = 0

    @property
    def height(self):

        return self.root.height if self.root else 0

    def find(self, key):

        found, node = self._find_or_parent(key)

        if found:
            return node

        return None

    def insert(self, key):

        found, parent = self._find_or_parent(key)

        if not found:
            node = Node(key, parent=parent)
            if parent:
                if parent.key > key:
                    parent.left = node
                else:
                    parent.right = node
            else:  # root node
                self.root = node
            self.size += 1
            self._rebalance(node)

    def insert_all(self, keys):

        for key in keys:
            self.insert(key)

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

    def _rotate_right(self, node):

        assert_node(node)
        assert_node(node.left)

        parent = node.parent
        new = node.left

        # 1
        if parent:
            if node.is_left_child():
                parent.left = new
            else:
                parent.right = new
            new.parent = parent
        else:
            self.root = new
            new.parent = None

        # 2
        node.left = new.right
        if node.left:
            node.left.parent = node

        # 3
        new.right = node
        node.parent = new

    def _rotate_left(self, node):

        assert_node(node)
        assert_node(node.right)

        parent = node.parent
        new = node.right

        # 1
        if parent:
            if node.is_left_child():
                parent.left = new
            else:
                parent.right = new
            new.parent = parent
        else:
            self.root = new
            new.parent = None

        # 2
        node.right = new.left
        if node.right:
            node.right.parent = node

        # 3
        new.left = node
        node.parent = new

    def _rebalance(self, node):

        assert_node(node)

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

        return f'<AVLTree: root={self.root} size={self.size} height=>'

    def __str__(self):

        return self.__repr__()


def print_as_list(node):

    print(f'{node} -> {node.left}, {node.right}')
