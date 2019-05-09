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

        tree.insert_all([4, 5, 3])

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

        tree.insert_all([4, 5, 3])

        self.assertEqual(tree.prev(tree.root).key, 3)

    def test_prev_empty(self):

        tree = TREE()

        self.assertRaises(AssertionError, tree.prev, tree.root)


if __name__ == '__main__':

    unittest.main()

