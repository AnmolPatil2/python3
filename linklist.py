class node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.tail = None


class ll:
    def __init__(self):
        self.head = None

    def pa(self):
        print(self.head.val)
        next = self.head
        for i in range(2):
            next = next.next
            print(next.val)

    def apendat(self, val, pos):
        c = 0
        next = self.head
        c += 1
        while(next.next != None):
            if(c-1 == pos):
                temp = next
                new = node(val)

                new.tail = next
                new.next = next.next
                next.next = new

                self.pa()

            else:
                next = next.next
                c += 1


if __name__ == '__main__':
    ll = ll()
    n = int(input(""))

    new = node(n)
    ll.head = new
    for _ in range(2):
        n = int(input(""))

        if(ll.head == None):
            new = node(n)
            head = new
            new.tail = head
        else:
            temp = new
            new = node(n)
            temp.next = new
            new.tail = temp
    ll.pa()
    ll.apendat(200, 2)
