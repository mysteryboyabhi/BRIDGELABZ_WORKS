"""Simple Balanced Parentheses
a. Desc -> Take an Arithmetic Expression such as
(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where parentheses are used to order the
performance of operations. Ensure parentheses must appear in a balanced
fashion.
b. I/P -> read in Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)
c. Logic -> Write a Stack Class to push open parenthesis “(“ and pop closed
parenthesis “)”. At the End of the Expression if the Stack is Empty then the"""

class Parenthesis:
    def is_bal(self,o, c):
        if o == "{" and c == "}":
            return True
        elif o == "[" and c == "]":
            return True
        elif o == "(" and c == ")":
            return True
        else:
            return False
    def To_bal(self,paren):
        s=Stack()
        is_balenced = True
        index = 0
        while index < len(paren) and is_balenced:
            if paren[index] in "({[":
                s.push(paren[index])
            else:
                if s.is_empty():
                    is_balenced = False
                elif paren[index] in ")}]":
                    top = s.pop()
                    if not self.is_bal(top, paren[index]):
                        is_balenced = False
                elif paren[index] in " * %/+-" and s.is_empty():
                    index+=1
                    continue
            index += 1
        if s.is_empty() and is_balenced:
            return True
        else:
            return False
class Stack:
    def __init__(self):
        self.item=[]

    def push(self, data):
        self.item.append(data)

    def pop(self):
        return self.item.pop()

    def is_empty(self):
        return self.item == []

    def value_in_stack(self):
        return self.item

paren=Parenthesis()
print(paren.To_bal("{8+8}(2-9)[]"))