class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
         self.head = None
         self.tail = None
         self.count = 0

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def enqueue(self, item):
        newNodo = Nodo(item)
        self.count += 1
        if self.head == None:
            self.head = newNodo
            self.tail = newNodo
            return
        self.tail.next = newNodo
        self.tail = newNodo
   

    def dequeue(self):
        if self.isEmpty() == False:
            temp_val = self.head
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            self.count -= 1
            return temp_val.data
        else:
            return None

    def __str__(self):
        if self.isEmpty() == False:
            actual = self.head
            nodos = ""
            while actual != None:
                nodos += f"{actual.data}\n"
                actual = actual.next
            return nodos
        else:
            return "ERROR! List is empty"
        
    def size(self):
        return self.count

def hotPotato(list_people, number_passes):
    temp_list = Queue()

    for i in list_people:
        temp_list.enqueue(i)
      

    while temp_list.size() > 1:
        for i in range(0, number_passes):
            people_removed = temp_list.dequeue()
            temp_list.enqueue(people_removed)
        eliminated = temp_list.dequeue()
        print(f"People: {eliminated} was eliminated")
     
    

    print(f"People: {temp_list} is the champion")
        

test = Queue()
test.enqueue("Alex")
test.enqueue("Sam")
test.enqueue("Lou")
print(test)

names = ["Alex", "Sam", "Lou"]
hotPotato(names, 2)
