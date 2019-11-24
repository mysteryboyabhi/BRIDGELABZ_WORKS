import math
def quadratic(a,b,c):
    d=b**2-(4*a*c)
    if d<0:
        delta=math.sqrt(abs(d))
        root1=str(-b/(2*a)) +str("+")+ (str(delta/(2*a))+str("j"))
        root2 = str(-b / (2 * a)) +str("-")+ (str(delta / (2 * a)) + str("j"))
        return root1,root2

    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    return round(root1,3),round(root2,3)
a,b,c=map(int,input("enter value of a,b,c seperated by comma: ").split(","))
print(quadratic(a,b,c))