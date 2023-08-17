class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        prev_node = self.tail
        self.tail = Node(data, None)

        if self.head is None:
            self.head = self.tail
        else:
            prev_node.next_node = self.tail

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        self.head = self.head.next_node

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return_str = ""
        node = self.head
        while node is not None:
            return_str = return_str + node.data + "\n"
            node = node.next_node

        return return_str[0:-1]
