def mechine(user_input_amount):
    try:
        user_input_amount=int(user_input_amount)
        if user_input_amount<=0:
            print("Sorry, you entered something wrong")
            return
        atm_has_notes=[1000,500,100,50,10,5,2,1]
        j=0
        count=0
        for note in atm_has_notes:
            if user_input_amount>=note:
                j=user_input_amount//note
                count+=j
                user_input_amount=user_input_amount-(j*note)
                print(f"{note} ka {j} note ")
        print(f"total number of notes is {count}")
    except ValueError:
        print("please enter number which should be in integer format")
amount=input("enter amount to withdraw: ")
mechine(amount)




