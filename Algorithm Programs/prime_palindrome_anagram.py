class Prime:
    def __init__(self):
        self.prime_list=[]
        self.anagram_and_palindrome_list=[]
        self.newlist=[]
    def prime_check(self,start,end):

        for item in range(start,end+1):
            prime=self.is_prime(item)
            if prime:
                self.prime_list.append(prime)
        return self.prime_list

    def is_prime(self,num):
        if num<2:
            return
        for i in range(2,num):
            if num%i==0:
                return
        else:
            return num
    def palindrome(self):
        for i in self.prime_list:
            palin=self.is_palindrome(i)
            if palin:
                self.anagram_and_palindrome_list.append(palin)
        return self.anagram_and_palindrome_list
    def is_palindrome(self,num):
        if num<100:
            return False
        if (str(num)==str(num)[::-1]):
            return num
    def anagram(self):
        for i in self.anagram_and_palindrome_list:
            for j in range(self.prime_list.index(i),len(self.prime_list)):
                if(sorted(str(i))==sorted(str(self.prime_list[j]))) and i!=self.prime_list[j]:
                    self.newlist.append(i)
                    self.newlist.append(self.prime_list[j])
        return self.newlist


prime=Prime()
start,end=map(int,input("enter range i.e, starting and end index seperated by space: ").split(" "))
print("Here is number which is prime ",prime.prime_check(start,end))
print("Here is number which is prime and palindrome",prime.palindrome())
print("Here is number which is prime palindrome and anagram as well: ",prime.anagram())