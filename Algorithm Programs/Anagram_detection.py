def check_anagram(w1,w2):
    if len(w1)!=len(w2):
        return False
    if sort(w1)==sort(w2):
        return True
    return False

def sort(arr):
    n=len(arr)
    arr=list(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

word1=input("enter first word: ")
word2=input("enter 2nd word: ")
print(check_anagram(word1,word2))






