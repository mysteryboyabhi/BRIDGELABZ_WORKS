def palindrome_check(str_arr):
    mylist=[]
    pal=""
    for i in str_arr:
        mylist.append(i)
    for i in range(len(mylist)):
        pal+=mylist.pop(len(mylist)-1)
    return pal==str_arr

print(palindrome_check())