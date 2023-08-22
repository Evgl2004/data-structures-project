"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestClassNode(unittest.TestCase):

    def test_init(self):
        node1 = Node("data1", None)
        node2 = Node(222, node1)

        self.assertEqual(node1.next_node, None)
        self.assertEqual(node2.next_node, node1)
        self.assertEqual(node2.data, 222)


class TestClassQueue(unittest.TestCase):

    def test_str(self):
        queue = Queue()

        self.assertEqual(str(queue), "")

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(str(queue), "data1\ndata2\ndata3")

    def test_enqueue(self):
        queue = Queue()

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data,'data3')
        self.assertEqual(queue.tail.next_node, None)

        with self.assertRaises(AttributeError):
            print(queue.tail.next_node.data)

    def test_dequeue(self):
        # Создаем пустую очередь
        queue = Queue()

        # Добавляем данных в очередь
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        assert queue.dequeue() == 'data1'
        assert queue.dequeue() == 'data2'
        assert queue.dequeue() == 'data3'
        assert queue.dequeue() is None
