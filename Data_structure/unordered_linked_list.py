f = open("demo.txt","r")

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=newnode

    def word_search(self,word):
        if self.head.data==word:
            new_head=self.head.next
            self.head.next=None
            self.head=new_head
            return
        cur = self.head
        prev=None
        while cur:

            if cur.data!=word:
                prev = cur
                cur = cur.next
            elif cur.data==word:
                prev.next=cur.next
                cur.next=None
                print("word found")
                return

        print("word not found")
        prev.next=Node(word)
    def print_and_update_demo1(self):
        cur=self.head
        with open('demo1.txt', 'w') as f:

            while cur:
                print(cur.data)
                f.write(str(cur.data)+" ")
                cur=cur.next




llist=LinkedList()
for data in f.readline().split():
    llist.append(data)

word=input("Enter the word to search form file: ")
llist.word_search(word)
llist.print_and_update_demo1()

f.close()
