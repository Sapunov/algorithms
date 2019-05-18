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

    def __repr__(self):

        return f'<BST: root={self.root} size={self.size}>'
