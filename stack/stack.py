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
            return None
        temp_val = self.head
        self.head = self.head.prev
        return temp_val.data

    def peek(self):
        if(self.isEmpty() == False):
            return self.head.data
        else:
            print("Stack is empty!")
            return None
  

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

def sort_stack(originalStack):
    temp_stack = Stack() 
    
    while originalStack.isEmpty() == False:
        temp_val = originalStack.pop()

        if temp_stack.isEmpty() == True:
            temp_stack.push(temp_val)
        else:
            while temp_stack.isEmpty() == False and temp_stack.peek() > temp_val:
                originalStack.push(temp_stack.pop())
            temp_stack.push(temp_val)

    while temp_stack.isEmpty() == False:
        originalStack.push(temp_stack.pop())

    print(f"\n================= Pilha temporaria: ==================")
    print(temp_stack)

   
test = Stack()
test.push(3)
test.push(2)
test.push(7)
test.push(9)
test.push(5)
print(test)

sort_stack(test)
print(f"\n================= Pilha Original: ==================")
print(test)
