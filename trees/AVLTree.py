from common import BinaryTree, Node, assert_node


class AVLNode(Node):

    def __init__(self, key, *, parent=None, left=None, right=None):

        super().__init__(key, parent=parent, left=left, right=right)

        self.height = 1

    @property
    def lheight(self):

        return self.left.height if self.has_left_child() else 0

    @property
    def rheight(self):

        return self.right.height if self.has_right_child() else 0

    def recompute_height(self):

        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0

        self.height = 1 + max(left_height, right_height)

    def __repr__(self):

        pkey = self.parent.key if self.parent else None
        diff = abs(self.lheight - self.rheight)

        return f'<Node:{self.key}^{pkey}@{self.height}[{diff}]>'


class AVLTree(BinaryTree):

    def __init__(self):

        self.root = None
        self.size = 0

    @property
    def height(self):

        return self.root.height if self.root else 0

    def insert(self, key):

        found, parent = self._find_or_parent(key)

        if not found:
            node = AVLNode(key, parent=parent)
            if parent is not None:
                if parent.key > key:
                    parent.left = node
                else:
                    parent.right = node
            else:  # root node
                self.root = node
            self.size += 1
            self._rebalance(node)

    def _rotate_right(self, node):

        assert_node(node)
        assert_node(node.left)

        # print(f'# Rotating right {node}...')

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

        # print(f'# Rotating left {node}...')

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

    def _rebalance_right(self, node):

        assert_node(node)

        # print(f'# Rebalancing right {node}...')

        middle = node.left

        if middle.rheight > middle.lheight:
            self._rotate_left(middle)

        self._rotate_right(node)

        node.recompute_height()
        middle.recompute_height()

    def _rebalance_left(self, node):

        assert_node(node)

        # print(f'# Rebalancing left {node}...')

        middle = node.right

        if middle.lheight > middle.rheight:
            self._rotate_right(middle)

        self._rotate_left(node)

        node.recompute_height()
        middle.recompute_height()

    def _rebalance(self, node):

        assert_node(node)

        # print(f'# Rebalancing {node}...')

        parent = node.parent

        if node.lheight > node.rheight + 1:
            self._rebalance_right(node)

        if node.rheight > node.lheight + 1:
            self._rebalance_left(node)

        node.recompute_height()

        if parent:
            self._rebalance(parent)

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

        return f'<AVLTree: root={self.root} size={self.size}>'

    def __str__(self):

        return self.__repr__()


def print_as_list(node):

    print(f'{node} -> {node.left}, {node.right}')
