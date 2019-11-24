"""from collections import stack
queue=deque([])
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.popleft()
print(queue)"""

class CashCounter:
    def __init__(self,cash_at_counter):
        self.cash_at_counter=cash_at_counter
        self.queue=[]
    def enque(self,what_to_do,data):
        self.queue.append((what_to_do,data))
    def deque(self):
        return self.queue.pop(0)
    def bal_cash_counetr(self):
        for item in range(len(self.queue)):
            first=self.deque()
            if first[0]=="D":
                self.cash_at_counter+=first[1]
            elif first[0]=="W":
                if self.cash_at_counter-first[1]<0:
                    print("cash is not available as much you need")
                    continue
                self.cash_at_counter -= first[1]
        return self.cash_at_counter

cs=CashCounter(10000)
cs.enque("W",10000)
cs.enque("D",1000)
cs.enque("W",10000)
cs.enque("W",10000)
cs.enque("D",1000)
print(cs.bal_cash_counetr())





