from sys import argv
def distance_form_origin(x,y):
    # Here x**2 denotes--> power of x is two
    return round((x**2+y**2)**0.5,4)

x,y=map(int,input("enter two points: ").split())
print(distance_form_origin(x,y))