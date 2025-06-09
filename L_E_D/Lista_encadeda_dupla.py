# Nó da lista
class Node:
    def __init__(self, data):
        self.data = data  # dado armazenado no nó
        self.next = None  # ponteiro para o próximo nó

# Lista encadeada simples
class LinkedList:
    def __init__(self):
        self.head = None  # início da lista

    # Inserir no final
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Imprimir a lista
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Inserir no início
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Remover um elemento
    def remove(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True  # encontrou e removeu
            previous = current
            current = current.next
        return False  # não encontrou

# Exemplo de uso
lista = LinkedList()
lista.append(10)
lista.append(20)
lista.insert_at_beginning(5)
lista.display()   # Saída esperada: 5 -> 10 -> 20 -> None

lista.remove(10)
lista.display()   # Saída esperada: 5 -> 20 -> None
