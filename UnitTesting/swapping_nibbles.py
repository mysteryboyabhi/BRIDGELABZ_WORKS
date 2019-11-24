"""Write Binary.py to read an i nteger as an Input, convert to Binary using toBinary
function and perform the following functions.
i. Swap nibbles and find the new number.
ii. Find the resultant number is the number is a power of 2.
A nibble is a four-bit aggregation, or half an octet. There are two nibbles in a byte.
Given a byte, swap the two nibbles i n i t. For example 100 i s to be represented as
01100100 i n a byte (or 8 bits). The two nibbles are (0110) and (0100). If we swap the
two nibbles, we get 01000110 which is 70 in decimal."""

def bin(num):
    rem=""
    while num:
        rem+=str(num%2)
        num=num//2
    n=len(rem)
    if n>8:
        print("Enter number in such a way that byte should be of 2")
        return False
    if n<8:
        final_after_add_zero=(8-n)*("0")+rem[::-1]
        return final_after_add_zero
    return rem[::-1]

def swap_nibble(number):
    bin_form=bin(number)
    final=0
    if bin_form:
        a,b=bin_form[:4],bin_form[4:]
        final=b+a
    # here type of final is string
    return convert_into_decimal(final)
def convert_into_decimal(number):
    # here type of number is string
    decimal_val=0
    n=len(number)-1
    for i in number:
        decimal_val+=int(i)*(2**n)
        n-=1
    return decimal_val


print(swap_nibble(int(input("Enter number to swap value: "))))