class No:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Bubble:
    def __init__(self):
        self.head = None
        self.tail = None

    def str(self):
        if (self.head == None):
            return print("Nothing in List!")
        actual = self.head
        while actual != None:
            print(actual.data)
            actual = actual.next

    def add(self, newValue):
        newNodo = No(newValue)
        if (self.head == None ):
            self.head = newNodo
            self.tail = newNodo
            return 
        self.tail.next = newNodo
        newNodo.previous = self.tail
        self.tail = newNodo
        return 

    def order(self):
        swap = True 
        while swap:
            swap = False 
            actual = self.head
            while actual != None and actual.next !=None:
                node_a = actual
                node_b = actual.next
                vizinho_esq = node_a.previous
                vizinho_dir = node_b.next

                if (node_a.data > node_b.data):
                    node_a.previous = node_b
                    node_b.next = node_a

                    if vizinho_dir:
                        node_a.next = vizinho_dir
                        vizinho_dir.previous = node_a
                    else:
                        self.tail = node_a
                        node_a.next = None

                    if vizinho_esq:
                        node_b.previous = vizinho_esq
                        vizinho_esq.next = node_b
                    else:
                        self.head = node_b
                        node_b.previous = None
                    swap = True
                else:
                    actual = node_b


    def order_simple(self):
        swap = True 
        while swap:
            swap = False 
            actual = self.head

            while actual != None and actual.next != None:

                if actual.data > actual.next.data:
                    temp = actual.data
                    actual.data = actual.next.data
                    actual.next.data = temp
                    swap = True
                actual = actual.next

value = Bubble()
value.add(15)
value.add(18)
value.add(19)
value.add(17)

value.str()
print(f"\n")
print(f"==============================")
print(f"\n")

value.order()

value.str()
