class No:
    def __init__(self, data):
        self.data = data
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, newData):
        newNodo = No(newData)
        if(self.isEmpty() == True):
            self.head = newNodo
            return
        newNodo.prev = self.head
        self.head = newNodo

    def pop(self):
        if(self.isEmpty() == True):
            print("Nothin to remove!")
            return 
        temp_val = self.head
        self.head = self.head.prev
        return temp_val.data

    def peek(self):
        if(self.isEmpty() == False):
            return self.head.data
        else:
            return "Stack is empty!"
  

    def __str__(self):
        actual = self.head
        values = ""
        count = 0
        if actual == None:
            return "Stack is empty!"
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
test.pop()
print(test)
