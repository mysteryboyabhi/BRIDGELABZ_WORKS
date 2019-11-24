def greetings(user_name):
    length_of_chr=len(user_name)
    if length_of_chr<3 :
        print(length_of_chr)
        print("Name must have a min val of 3 char: ")
        return
    print(f"Hello {user_name} its me Abhishek how are you ?")

greetings(input("Enter the user name: "))