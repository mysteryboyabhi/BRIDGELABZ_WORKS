def leap(user_input_year):

    if user_input_year<1000:
        print(f"your entered year is {user_input_year} that is not a four digit number. SO, please enter four digit number")
        return
    if user_input_year%400==0 or user_input_year%4==0 and user_input_year%100!=0:
        print(f"yes, {user_input_year} is a leap year ")
    else:
        print(f"NO, {user_input_year} is not a leap year")

leap(int(input("Enter Year: ")))