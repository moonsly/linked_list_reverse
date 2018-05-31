#!/usr/bin/python3
import os
import filecmp
import unittest

from linked_list_reverse import LinkedList


class LinkedListTest(unittest.TestCase):

    def test_init_empty_llist(self):
        empty = LinkedList()
        self.assertEqual(empty.val, None)
        self.assertEqual(empty.nxt, None)
        self.assertEqual(str(empty), '[None]')

    def test_init_all_variants(self):
        llist = LinkedList()
        self.assertEqual(llist.val, None)
        self.assertEqual(llist.nxt, None)
        self.assertEqual(str(llist), '[None]')

        llist = LinkedList(lst=[])
        self.assertEqual(llist.val, None)
        self.assertEqual(llist.nxt, None)
        self.assertEqual(str(llist), '[None]')

        llist = LinkedList(0, None)
        self.assertEqual(llist.val, 0)
        self.assertEqual(llist.nxt, None)
        self.assertEqual(str(llist), '[0]')

        l1 = LinkedList(1, None)
        llist = LinkedList(0, l1)
        self.assertEqual(llist.val, 0)
        self.assertEqual(llist.nxt, l1)
        self.assertEqual(llist.nxt.val, 1)
        self.assertEqual(llist.nxt.nxt, None)
        self.assertEqual(str(llist), '[0, 1]')

        llist = LinkedList(lst=[1, 2])
        self.assertEqual(llist.val, 1)
        self.assertEqual(llist.nxt.val, 2)
        self.assertEqual(llist.nxt.nxt, None)
        self.assertEqual(str(llist), '[1, 2]')

        llist = LinkedList([1, 2])
        self.assertEqual(llist.val, 1)
        self.assertEqual(llist.nxt.val, 2)
        self.assertEqual(llist.nxt.nxt, None)
        self.assertEqual(str(llist), '[1, 2]')

    def test_push_pop(self):
        llist = LinkedList([1, 2])
        push_res = llist.push_last(3)
        self.assertEqual(push_res, True)
        self.assertEqual(str(llist), '[1, 2, 3]')

        push_res = llist.push_last({1: 3})
        self.assertEqual(push_res, True)
        self.assertEqual(str(llist), '[1, 2, 3, {1: 3}]')

        pop_res = llist.pop_last()
        self.assertEqual(pop_res, {1: 3})
        self.assertEqual(str(llist), '[1, 2, 3]')

        pop_res = llist.pop_last()
        self.assertEqual(pop_res, 3)
        self.assertEqual(str(llist), '[1, 2]')

        pop_res = llist.pop_last()
        self.assertEqual(pop_res, 2)
        self.assertEqual(str(llist), '[1]')

        pop_res = llist.pop_last()
        self.assertEqual(pop_res, 1)
        self.assertEqual(str(llist), '[None]')

        pop_res = llist.pop_last()
        self.assertEqual(pop_res, None)
        self.assertEqual(str(llist), '[None]')

    def test_reverse(self):
        llist = LinkedList([1, 2])
        res = list(llist.reverse())
        self.assertEqual(res, [2, 1])

        llist = LinkedList(lst=[])
        res = list(llist.reverse())
        self.assertEqual(res, [None])

        llist = LinkedList(lst=[0])
        res = list(llist.reverse())
        self.assertEqual(res, [0])

        llist = LinkedList(lst=[1, 2, {}])
        res = list(llist.reverse())
        self.assertEqual(res, [{}, 2, 1])

        l1000 = list(range(1000))
        llist = LinkedList(lst=l1000)
        res = list(llist.reverse())
        self.assertEqual(res, list(reversed(l1000)))

        l10000 = list(range(10000)) + [{1}]
        llist = LinkedList(lst=l10000)
        res = list(llist.reverse())
        self.assertEqual(res, list(reversed(l10000)))


if __name__ == '__main__':
    unittest.main()
