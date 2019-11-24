from sys import argv
def power_of_two(N):
    if N>30:
        print("since 2^31 overflows an int, So enter number less than 31")
        return
    i=1
    while i<N:
        print(f"{i}th power is: {2**i}")
        i+=1

power_of_two(int(input("enter number to write table of two: ")))