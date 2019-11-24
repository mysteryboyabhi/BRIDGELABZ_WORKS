
def day_of_week(m,d,y):
    if m<=0 or m>12 or d<=0 or d>31 or y<1000 or y>9999:
        return "enter wisely wrong input"
    y0=y-(14-m)//12
    x=y0+y0//4-y0//100 + y0//400
    m0=m+12*((14-m)//12)-2
    d0=(d+x+(31*m0)//12)%7
    day_dict={0:"sunday",1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday",6:"saturday"}
    return day_dict[d0]
m,d,y=map(int,input("enter month date and year: ").split())
print(day_of_week(m,d,y))