class No:
    def __init__(self, data):
        self.data = data
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, newData):
        newNodo = No(newData)
        if(self.head == None):
            self.head = newNodo
            return
        newNodo.prev = self.head
        self.head = newNodo

    def pop(self):
        if(self.head == None):
            print("Nothin to remove!")
            return 
        self.head = self.head.prev

    def __str__(self):
        actual = self.head
        values = ""
        count = 0
        if actual == None:
            print("Stack is empty!")
            return
        while actual != None:
            values += f"position:({count}) - value: {actual.data}\n"
            count += 1
            actual = actual.prev
        return values
    
test = Stack()
test.push(1)
test.push(2)
test.push(3)
test.push(4)
test.push(5)
print(test)
test.pop()
test.pop()
print(test)
