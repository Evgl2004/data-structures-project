class Node:
    """Класс для узла односвязного списка"""
    __slots__ = ('data', 'next_node')

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""
    __slots__ = ('head', 'tail')

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        next_node = self.head
        self.head = Node(data)
        self.head.next_node = next_node

        if self.tail is None:
            self.tail = self.head

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        prev_node = self.tail
        self.tail = Node(data)

        if self.head is None:
            self.head = self.tail
        else:
            prev_node.next_node = self.tail

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string[1:]
