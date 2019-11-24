def convert_tem(user_data,convert_into):
    if convert_into=="F":
        return f" Farenhite tem is  {(user_data *( 9 / 5)) + 32}"

    elif convert_into=="C":
        return f" Celsius tem is  {(user_data -32) * 5/9}"
    else:
        return "please pick C or F for Celsius or Farenhite respectively"
temp=int(input("Enter temperature: "))
convert_into=input("choose F or C: ").upper()
print(convert_tem(temp,convert_into))