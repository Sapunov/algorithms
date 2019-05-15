import random

from common import BinaryTree, assert_node


class BSTree(BinaryTree):

    def insert_all(self, keys, *, use_random=True):

        if use_random:
            if not isinstance(keys, list):
                keys = list(keys)
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

    def __repr__(self):

        return f'<BST: root={self.root} size={self.size}>'
