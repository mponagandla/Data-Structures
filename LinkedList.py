class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAtStart(self, data):
        if self.head == None:
            node = Node(data, next = self.head)
            self.head = node
            self.tail = node
        else:
            node = Node(data, self.head)
            self.head = node

    def insertAtEnd(self, data):
        if self.head == None:
            node = Node(data,prev = self.tail)
            self.head = node
            self.tail = node
            print("none")
            return
        node = Node(data,prev = self.tail)
        self.tail.next = node
        self.tail = node


    def printLL(self):
        if self.head == None:
            print("List Empty")
            return
        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtStart(10)
    ll.insertAtStart(11)
    ll.insertAtStart(12)
    ll.insertAtEnd(9)
    #ll.insertAtEnd(10)
    ll.printLL()