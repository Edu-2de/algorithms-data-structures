class No:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Selection:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, newValue):
        newNodo = No(newValue)
        if(self.head == None):
            self.head = newNodo
            self.tail = newNodo
            return
        if(self.head.next == None):
            self.head.next = newNodo
            newNodo.prev = self.head
            self.tail = newNodo
            return
        self.tail.next = newNodo
        newNodo.prev = self.tail
        self.tail = newNodo

    def __str__(self):
        actual = self.head
        result = ""
        count = 0
        while actual != None:
            address = hex(id(actual))
            result += f"position: {count} - address: {address[-5:]} - value: {actual.value}\n"
            actual = actual.next
            count += 1
        return result

    def OrderSelection(self):
        actual = self.head

        while actual != None:
            less = actual
            nextNodo = actual.next

            while nextNodo != None:
                if(nextNodo.value < less.value):
                    less = nextNodo
                    print(f"Actual lowest value: {less.value}")
                nextNodo = nextNodo.next

            if(actual != less):
                prevActual = actual.prev
                nextActual = actual.next
                prevLess = less.prev
                nextLess = less.next

                if actual.next == less:
                    less.prev = prevActual
                    less.next = actual
                    actual.prev = less
                    actual.next = nextLess

                    if prevActual != None: prevActual.next = less
                    if nextLess != None: nextLess.prev = actual
                else:
                    less.prev = prevActual
                    less.next = nextActual
                    actual.prev = prevLess
                    actual.next = nextLess

                    if prevActual != None: prevActual.next = less
                    if nextActual != None: nextActual.prev = less
                    if prevLess != None: prevLess.next = actual
                    if nextLess != None: nextLess.prev = actual
                if self.head == actual: 
                    self.head = less

                if self.tail == less: 
                    self.tail = actual

                actual = less

            actual = actual.next
        print(f"\nThe lowest final value: {less.value}\n")



firstTest = Selection()
firstTest.push(5)
firstTest.push(9)
firstTest.push(3)
firstTest.push(9)
firstTest.push(2)
firstTest.push(1)

print(firstTest)

firstTest.OrderSelection()

print(firstTest)
