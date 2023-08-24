"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import  Node, LinkedList


class TestClassNode(unittest.TestCase):
    def test_init(self):
        node = Node({'id': 1})

        self.assertEqual(node.data, {'id': 1})
        self.assertEqual(node.next_node, None)


class TestClassLinkedList(unittest.TestCase):
    def test_init(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 1})
        linked_list.insert_at_end({'id': 2})

        self.assertEqual(linked_list.tail.data, {'id': 2})

        linked_list_two = LinkedList()
        linked_list_two.insert_at_end({'id': 2})

        self.assertEqual(linked_list_two.head.data, {'id': 2})

    def test_str(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 1})
        self.assertEqual(str(linked_list), "{'id': 1} -> None")

        linked_list.insert_beginning({'id': 2})
        self.assertEqual(str(linked_list), "{'id': 2} -> {'id': 1} -> None")