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

    def test_to_list(self):
        # Создаем и наполняем односвязный список
        linked_list = LinkedList()

        linked_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        linked_list.insert_at_end({'id': 2, 'username': 'mik.roz'})
        linked_list.insert_at_end({'id': 3, 'username': 'mosh_s'})
        linked_list.insert_beginning({'id': 0, 'username': 'serebro'})

        # метод to_list()
        lst = linked_list.to_list()
        self.assertEqual(str(lst[0]), "{'id': 0, 'username': 'serebro'}")
        self.assertEqual(str(lst[1]), "{'id': 1, 'username': 'lazzy508509'}")
        self.assertEqual(str(lst[2]), "{'id': 2, 'username': 'mik.roz'}")
        self.assertEqual(str(lst[3]), "{'id': 3, 'username': 'mosh_s'}")

    def test_get_data_by_id(self):
        # Создаем и наполняем односвязный список
        linked_list = LinkedList()

        linked_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        linked_list.insert_at_end({'id': 2, 'username': 'mik.roz'})
        linked_list.insert_at_end({'id': 3, 'username': 'mosh_s'})
        linked_list.insert_beginning({'id': 0, 'username': 'serebro'})

        # метод get_data_by_id()
        user_data = linked_list.get_data_by_id(3)
        self.assertEqual(user_data, {'id': 3, 'username': 'mosh_s'})

        user_data = linked_list.get_data_by_id(4)
        self.assertEqual(user_data, None)

    def test_err_get_data_by_id(self):
        # работа блока try/except
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        linked_list.insert_at_end('idusername')

        user_data = linked_list.get_data_by_id(2)
        self.assertEqual(user_data, None)

        linked_list.insert_at_end([1, 2, 3])
        linked_list.insert_at_end({'id': 2, 'username': 'mosh_s'})

        user_data = linked_list.get_data_by_id(2)

        self.assertEqual(user_data, {'id': 2, 'username': 'mosh_s'})
