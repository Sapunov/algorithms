from unittest import TestCase
import unittest

import binarySearchTree


TREE = binarySearchTree.BinarySearchTree


class BSTTest(TestCase):

    def test_insert(self):

        tree = TREE()

        self.assertEqual(tree.size, 0)

        tree.insert('test')

        self.assertEqual(tree.size, 1)

    def test_insert_all(self):

        tree = TREE()
        tree.insert_all([1, 2, 3, 4])

        self.assertEqual(tree.size, 4)

    def test_next_middle(self):

        tree = TREE()

        tree.insert_all([7, 5, 4, 1])

        five = tree.find(5)

        self.assertEqual(tree.next(five).key, 7)

    def test_next_last(self):

        tree = TREE()

        tree.insert_all([7, 5, 4, 1])

        seven = tree.find(7)

        self.assertIsNone(tree.next(seven))

    def test_next_root(self):

        tree = TREE()

        tree.insert_all([4, 5, 3], use_random=False)

        self.assertEqual(tree.next(tree.root).key, 5)

    def test_next_empty(self):

        tree = TREE()

        self.assertRaises(AssertionError, tree.next, tree.root)

    def test_find_or_parent_none(self):

        tree = TREE()

        tree.insert_all([4, 3, 2])

        found, node = tree._find_or_parent(6)

        self.assertFalse(found)
        self.assertEqual(node.key, 4)

    def test_find_or_parent_found(self):

        tree = TREE()

        tree.insert_all([4, 3, 2])

        found, node = tree._find_or_parent(4)

        self.assertTrue(found)
        self.assertEqual(node.key, 4)

    def test_find_or_parent_empty(self):

        tree = TREE()

        found, node = tree._find_or_parent(4)

        self.assertFalse(found)
        self.assertIsNone(node)

    def test_find_found(self):

        tree = TREE()

        tree.insert_all([5, 4, 3])

        node = tree.find(4)

        self.assertEqual(node.key, 4)

    def test_find_not_found(self):

        tree = TREE()

        tree.insert_all([5, 4, 3])

        node = tree.find(56)

        self.assertIsNone(node)


    def test_find_range(self):

        tree = TREE()

        tree.insert_all([9, 8, 7, 5, 4, 2, 1])

        found = tree.find_range(3, 7)
        keys = [_.key for _ in found]

        self.assertEqual(len(keys), 3)
        self.assertEqual(keys, [4, 5, 7])

    def test_find_range_not_found(self):

        tree = TREE()

        tree.insert_all([9, 8, 7, 5, 4, 2, 1])

        found = tree.find_range(10, 34)

        self.assertEqual(len(found), 0)

    def test_prev_middle(self):

        tree = TREE()

        tree.insert_all([7, 5, 4, 1])

        five = tree.find(5)

        self.assertEqual(tree.prev(five).key, 4)

    def test_prev_first(self):

        tree = TREE()

        tree.insert_all([7, 5, 4, 1])

        one = tree.find(1)

        self.assertIsNone(tree.prev(one))

    def test_prev_root(self):

        tree = TREE()

        tree.insert_all([4, 5, 3], use_random=False)

        self.assertEqual(tree.prev(tree.root).key, 3)

    def test_prev_empty(self):

        tree = TREE()

        self.assertRaises(AssertionError, tree.prev, tree.root)

    def test_dfs(self):

        tree = TREE()
        tree.insert_all([2, 1, 0, 9, 5], use_random=False)

        keys = []
        tree.dfs(lambda node: keys.append(node.key))

        self.assertEqual(keys, [2, 1, 0, 9, 5])

    def test_dfs_empty(self):

        tree = TREE()

        keys = []
        tree.dfs(lambda node: keys.append(node.key))

        self.assertEqual(keys, [])

    def test_bfs(self):

        tree = TREE()
        tree.insert_all([2, 1, 0, 9, 5], use_random=False)

        keys = []
        tree.bfs(lambda node: keys.append(node.key))

        self.assertEqual(keys, [2, 1, 9, 0, 5])

    def test_bfs_empty(self):

        tree = TREE()

        keys = []
        tree.bfs(lambda node: keys.append(node.key))

        self.assertEqual(keys, [])

    def test_delete_not_children(self):

        tree = TREE()

        tree.insert_all([5, 2, 9])

        tree.delete_by_key(9)

        self.assertEqual(tree.keys(), [2, 5])

    def test_delete_left_child(self):

        tree = TREE()

        tree.insert_all([5, 2, 9, 1])

        tree.delete_by_key(2)

        self.assertEqual(tree.keys(), [1, 5, 9])

    def test_delete_right_child(self):

        tree = TREE()

        tree.insert_all([5, 2, 9, 3])

        tree.delete_by_key(2)

        self.assertEqual(tree.keys(), [3, 5, 9])

    def test_delete_root_with_children(self):

        tree = TREE()

        tree.insert_all([5, 2, 9])

        tree.delete_by_key(5)

        self.assertEqual(tree.keys(), [2, 9])

    def test_delete_root_with_one_child(self):

        tree = TREE()

        tree.insert_all([5, 2])

        tree.delete_by_key(5)

        self.assertEqual(tree.keys(), [2])

    def test_delete_root_no_children(self):

        tree = TREE()

        tree.insert_all([5])

        tree.delete_by_key(5)

        self.assertEqual(tree.keys(), [])

    def test_delete_both_children(self):

        tree = TREE()

        tree.insert_all([5, 3, 9, 1, 4], use_random=False)

        tree.delete_by_key(3)

        keys = []
        tree.dfs(lambda node: keys.append(node.key))

        self.assertEqual(keys, [5, 4, 1, 9])

    def test_min(self):

        tree = TREE()

        tree.insert_all([5, 3, 9, 1, 4])

        self.assertEqual(tree.min().key, 1)

    def test_min_empty(self):

        tree = TREE()

        self.assertIsNone(tree.min())

    def test_min_node(self):

        tree = TREE()

        tree.insert_all([5, 3, 9, 8, 23], use_random=False)

        nine = tree.find(9)
        self.assertEqual(tree.min(nine).key, 8)

    def test_max(self):

        tree = TREE()

        tree.insert_all([5, 3, 9, 1, 4])

        self.assertEqual(tree.max().key, 9)

    def test_max_empty(self):

        tree = TREE()

        self.assertIsNone(tree.max())

    def test_max_node(self):

        tree = TREE()

        tree.insert_all([5, 3, 9, 8, 23], use_random=False)

        nine = tree.find(9)
        self.assertEqual(tree.max(nine).key, 23)

    def test_inorder_ok(self):

        tree = TREE()
        tree.insert_all([5, 3, 9, 8, 23])

        keys = []
        tree.inorder(lambda node: keys.append(node.key))

        self.assertEqual(keys, [3, 5, 8, 9, 23])

    def test_inorder_empty(self):

        tree = TREE()

        keys = []
        tree.inorder(lambda node: keys.append(node.key))

        self.assertEqual(keys, [])

'''
    5
   / \
  3   9
     / \
    8   23
'''

if __name__ == '__main__':

    unittest.main()

