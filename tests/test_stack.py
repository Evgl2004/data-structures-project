"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestClassNode(unittest.TestCase):

    def test_init(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.next_node, None)
        self.assertEqual(n2.next_node, n1)


class TestClassStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        self.assertEqual(stack.top.data, "data3")
        self.assertEqual(stack.top.next_node.data, "data2")
        self.assertEqual(stack.top.next_node.next_node.data, "data1")
        self.assertEqual(stack.top.next_node.next_node.next_node, None)

        with self.assertRaises(AttributeError):
            print(stack.top.next_node.next_node.next_node.data)