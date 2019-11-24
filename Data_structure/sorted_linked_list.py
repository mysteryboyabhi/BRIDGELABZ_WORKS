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
        if self.head.data>=data:
            newnode.next=self.head
            self.head=newnode
            return
        cur=self.head
        prev=None
        while cur.next:
            if cur.data<=data and data<=cur.next.data:
                newnode.next=cur.next
                cur.next=newnode
                return
            cur=cur.next
        if cur.data<data:
            cur.next=newnode

    def print_and_update_demo1(self):
        cur=self.head
        with open("demo1.txt","w") as f:
            while cur:
                print(cur.data)
                f.write(str(cur.data) + " ")
                cur = cur.next


    def word_search(self,word):
        if self.head.data==word:
            new_head=self.head.next
            self.head.next=None
            self.head=new_head
            print("word found thats why i'm gonna remove the word from list")
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
                print("word found thats why i'm gonna remove the word from list")
                return
        print("Word Not Found and hence it is added at the end of list")
        prev.next=Node(word)

f = open("demo.txt","r")
mylist=f.readline().split()
llist=LinkedList()
for i in mylist:
    llist.append(i)
word=input("Enter the word you wanna search in list: ")
llist.word_search(word)
llist.print_and_update_demo1()
f.close()