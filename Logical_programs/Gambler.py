# class Leap:
#     def leapyear(self,year):
#         if year<1000: return "Year must be four digit number"
#         elif year%4==0 or year%400==0 and year%100!=0:return f"{year} is Leap a leap year"
#         else: return f"{year} is not a leap year"
#
##------------------------------------------------------------------------------------------------
# l=Leap()
# print(l.leapyear(1752))
# def power_of_two(num):
#     i=1
#     while i<=num:
#         new_number=2**i
#         print(new_number)
#         i+=1
#
# power_of_two(4)

#------------------------------------------------------------------------------------------------
# def nth_harmmonic(N):
#     for i in range(1,N+1):
#         if i<N:
#             print("1"+"/"+str(i)+" + ",end="")
#         else:
#             print("1" + "/" + str(i))
#
# nth_harmmonic(6)
#---------------------------------------------------------------------------------------------------------------------

def prime_factorisation(number):
    while number%2==0:
        print(2)
        number=number//2
    for i in range(3,int(number**(0.5))+1,2):
        while number%i==0:
            print(i)
            number=number/i
    if number>2:
        print(number)
prime_factorisation(1092)













